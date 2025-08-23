try:
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    result = a / b
    print("Результат ділення:", result)
except ValueError:
    print("Помилка: введене значення не є числом!")
except ZeroDivisionError:
    print("Помилка: ділення на нуль!")
finally:
    print("Операція завершена.")



numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Введіть індекс елемента: "))
    print("Елемент за індексом", index, ":", numbers[index])
except ValueError:
    print("Помилка: індекс повинен бути числом!")
except IndexError:
    print("Помилка: індекс виходить за межі списку!")
finally:
    print("Операція завершена.")





try:
    sales = input("Введіть дані про продажі через пробіл: ")
    sales_list = list(map(float, sales.split()))
    total = sum(sales_list)
    print("Загальна сума продажів:", total)
except ValueError:
    print("Помилка: введено некоректні дані!")
finally:
    print("Обробка завершена.")



import math

try:
    num = float(input("Введіть число: "))
    if num < 0:
        raise Exception("Не можна обчислити квадратний корінь від'ємного числа")
    result = math.sqrt(num)
    print("Квадратний корінь:", result)
except ValueError:
    print("Помилка: введене значення не є числом!")
except Exception as e:
    print("Помилка:", e)
finally:
    print("Обчислення завершено.")





try:
    data = input("Введіть дані (назва, ціна, кількість): ")
    name, price, quantity = data.split(",")
    name = name.strip()
    price = float(price.strip())
    quantity = int(quantity.strip())
    print(f"Товар: {name}, Ціна: {price}, Кількість: {quantity}")
except ValueError:
    print("Помилка: некоректні дані! Переконайтеся, що ціна та кількість є числами.")
finally:
    print("Парсинг завершено.")

