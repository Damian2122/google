
lines = []
for i in range(3):
    line = input(f"Введіть рядок {i + 1}: ")
    lines.append(line)


with open("data.txt", "w", encoding="utf-8") as file:
    for line in lines:
        file.write(line + "\n")

print("Рядки успішно записано у файл data.txt.")


import os


if os.path.exists("data.txt"):
    print("Файл 'data.txt' існує. Виводжу кожен другий рядок:\n")

    with open("data.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()


    for i in range(1, len(lines), 2):
        print(lines[i].strip())

else:
    print("Файл 'data.txt' не знайдено.")
