import time
import os
import threading
from gtts import gTTS
from playsound import playsound
import uuid


def speak(text):
    filename = f"say_{uuid.uuid4().hex}.mp3"  # унікальне ім'я файлу
    tts = gTTS(text=text, lang='uk')
    tts.save(filename)
    playsound(filename)
    os.remove(filename)  # видаляємо після відтворен

class Tom:
    def __init__(self):
        self.eat = 100
        self.health = 100
        self.toilet = 100
        self.clean = 100
        self.alive = True

    def speak(self, text):
        """Озвучити текст через gTTS з автоматичним видаленням"""
        filename = f"say_{uuid.uuid4().hex}.mp3"
        tts = gTTS(text=text, lang='uk')
        tts.save(filename)

        def play_and_remove():
            playsound(filename)
            os.remove(filename)

        threading.Thread(target=play_and_remove, daemon=True).start()

    def decrease_stats(self):
        while self.alive:
            self.eat -= 1
            self.health -= 1
            self.toilet -= 1
            self.clean -= 1
            self.show_stats()

            if self.eat <= 0 or self.health <= 0 or self.toilet <= 0 or self.clean <= 0:
                print("❌ Tom помер... Гру закінчено.")
                self.speak("Я помер... Гру закінчено")
                self.alive = False
                break

            time.sleep(1)

    def show_stats(self):
        print(f"Eat: {self.eat}, Health: {self.health}, Toilet: {self.toilet}, Clean: {self.clean}")

    # дії гравця зі звуком
    def feed(self):
        self.eat = min(100, self.eat + 10)
        print("🍗 Tom поїв!")
        self.speak("Мммммммммм, бульба з кропом і тушонка засмальцьована!")

    def heal(self):
        self.health = min(100, self.health + 10)
        print("💊 Tom підлікувався!")
        self.speak("я ібупрофен короче схавав лежу кайфую!")

    def go_to_toilet(self):
        self.toilet = min(100, self.toilet + 10)
        print("🚽 Tom сходив у туалет!")
        self.speak("бульк")

    def wash(self):
        self.clean = min(100, self.clean + 10)
        print("🧼 Tom помився!")
        self.speak("вмивсі тебер тако пахнєчо пахну а не потом")


def player_input(tom):
    while tom.alive:
        action = input("Введи дію (feed / heal / toilet / wash): ").strip().lower()
        if action == "feed":
            tom.feed()
        elif action == "heal":
            tom.heal()
        elif action == "toilet":
            tom.go_to_toilet()
        elif action == "wash":
            tom.wash()
        else:
            print("❓ Невідома команда!")


tom = Tom()

# потік для зниження параметрів
threading.Thread(target=tom.decrease_stats, daemon=True).start()
# потік для введення команд гравця
threading.Thread(target=player_input, args=(tom,), daemon=True).start()

while tom.alive:
    time.sleep(0.1)
