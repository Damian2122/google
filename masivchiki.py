text = input("Введіть текст: ")

# Речення закінчуються на ".", "!", "?"
end_symbols = ".!?"
count = 0

for char in text:
    if char in end_symbols:
        count += 1

print("Кількість речень у тексті:", count)









text = input("Введіть рядок: ")

clean_text = ''.join(char.lower() for char in text if char.isalnum())

is_palindrome = clean_text == clean_text[::-1]

if is_palindrome:
    print("Це паліндром.")
else:
    print("Це не паліндром.")








text = input("Введіть текст: ")
reserved = {"if", "else", "while", "for", "return", "break", "continue", "def", "class", "import"}

words = text.split()
new_words = []

for word in words:
    word_clean = word.strip(".,!?()")
    if word_clean in reserved:
        new_words.append(word.replace(word_clean, word_clean.upper()))
    else:
        new_words.append(word)

new_text = ' '.join(new_words)
print("Змінений текст:", new_text)










text = input("Введіть рядок: ")
char1 = input("Перший символ: ")
char2 = input("Другий символ: ")

index1 = text.find(char1)
index2 = text.find(char2)

if index1 != -1 and index2 != -1 and index1 < index2:
    result = text[:index1] + text[index2 + 1:]
    print("Результат:", result)
else:
    print("Символи не знайдено або у неправильному порядку.")









text = input("Введіть текст: ")
bad_chars = input("Введіть символи (без пробілів): ")

words = text.split()
filtered_words = []

for word in words:
    if not any(char in word for char in bad_chars):
        filtered_words.append(word)

result = ' '.join(filtered_words)
print("Результат:", result)









text = input("Введіть текст: ")

words = text.split()
reversed_words = words[::-1]

result = ' '.join(reversed_words)
print("Зворотний текст:", result)
