from datetime import datetime

# === МОДЕЛІ ===
class Employee:
    def __init__(self, full_name, position, phone, email):
        self.full_name = full_name
        self.position = position
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.full_name}, {self.position}, {self.phone}, {self.email}"


class Car:
    def __init__(self, manufacturer, year, model, cost_price, sale_price):
        self.manufacturer = manufacturer
        self.year = year
        self.model = model
        self.cost_price = cost_price
        self.sale_price = sale_price

    def __str__(self):
        return f"{self.manufacturer} {self.model} ({self.year}), собівартість {self.cost_price}, ціна {self.sale_price}"


class Sale:
    def __init__(self, employee, car, date, real_price):
        self.employee = employee
        self.car = car
        self.date = date
        self.real_price = real_price

    def __str__(self):
        return f"{self.date}: {self.employee.full_name} продав {self.car.model} за {self.real_price}"


# === РЕПОЗИТОРІЙ ===
class Repository:
    def __init__(self):
        self.employees = []
        self.cars = []
        self.sales = []

    # --- CRUD ---
    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, name):
        new_employees = []
        for e in self.employees:
            if e.full_name != name:
                new_employees.append(e)
        self.employees = new_employees

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, model):
        new_cars = []
        for c in self.cars:
            if c.model != model:
                new_cars.append(c)
        self.cars = new_cars

    def add_sale(self, sale):
        self.sales.append(sale)

    def remove_sale(self, index):
        if 0 <= index < len(self.sales):
            self.sales.pop(index)

    # --- LIST ---
    def list_employees(self):
        if not self.employees:
            return "Немає співробітників"
        result = ""
        for e in self.employees:
            result += str(e) + "\n"
        return result.strip()

    def list_cars(self):
        if not self.cars:
            return "Немає авто"
        result = ""
        for c in self.cars:
            result += str(c) + "\n"
        return result.strip()

    def list_sales(self):
        if not self.sales:
            return "Немає продажів"
        result = ""
        for i in range(len(self.sales)):
            result += f"{i}. {self.sales[i]}\n"
        return result.strip()

    # --- REPORTS ---
    def all_sales_by_employee(self, employee_name):
        result = ""
        for s in self.sales:
            if s.employee.full_name == employee_name:
                result += str(s) + "\n"
        if result == "":
            return "Немає даних"
        return result.strip()

    def most_sold_car(self, start_date, end_date):
        filtered = []
        for s in self.sales:
            s_date = datetime.strptime(s.date, "%Y-%m-%d")
            if start_date <= s_date <= end_date:
                filtered.append(s)
        if not filtered:
            return "Немає даних"
        counts = {}
        for s in filtered:
            if s.car.model not in counts:
                counts[s.car.model] = 0
            counts[s.car.model] += 1
        max_count = -1
        best_car = ""
        for model, count in counts.items():
            if count > max_count:
                max_count = count
                best_car = model
        return best_car

    def best_seller(self, start_date, end_date):
        filtered = []
        for s in self.sales:
            s_date = datetime.strptime(s.date, "%Y-%m-%d")
            if start_date <= s_date <= end_date:
                filtered.append(s)
        if not filtered:
            return "Немає даних"
        profits = {}
        for s in filtered:
            profit = s.real_price - s.car.cost_price
            if s.employee.full_name not in profits:
                profits[s.employee.full_name] = 0
            profits[s.employee.full_name] += profit
        max_profit = -1
        best_emp = ""
        for name, profit in profits.items():
            if profit > max_profit:
                max_profit = profit
                best_emp = name
        return best_emp

    def total_profit(self, start_date, end_date):
        total = 0
        for s in self.sales:
            s_date = datetime.strptime(s.date, "%Y-%m-%d")
            if start_date <= s_date <= end_date:
                total += s.real_price - s.car.cost_price
        return total

    # --- FILES ---
    def save(self, filename="data.txt"):
        f = open(filename, "w", encoding="utf-8")
        for e in self.employees:
            f.write("EMPLOYEE|" + e.full_name + "|" + e.position + "|" + e.phone + "|" + e.email + "\n")
        for c in self.cars:
            f.write("CAR|" + c.manufacturer + "|" + str(c.year) + "|" + c.model + "|" + str(c.cost_price) + "|" + str(c.sale_price) + "\n")
        for s in self.sales:
            f.write("SALE|" + s.employee.full_name + "|" + s.car.model + "|" + s.date + "|" + str(s.real_price) + "\n")
        f.close()

    def load(self, filename="data.txt"):
        try:
            f = open(filename, "r", encoding="utf-8")
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 0:
                    continue
                if parts[0] == "EMPLOYEE":
                    self.employees.append(Employee(parts[1], parts[2], parts[3], parts[4]))
                elif parts[0] == "CAR":
                    self.cars.append(Car(parts[1], int(parts[2]), parts[3], float(parts[4]), float(parts[5])))
                elif parts[0] == "SALE":
                    emp = None
                    car = None
                    for e in self.employees:
                        if e.full_name == parts[1]:
                            emp = e
                            break
                    for c in self.cars:
                        if c.model == parts[2]:
                            car = c
                            break
                    if emp and car:
                        self.sales.append(Sale(emp, car, parts[3], float(parts[4])))
            f.close()
        except FileNotFoundError:
            pass


# === МЕНЮ ===
def menu():
    repo = Repository()
    repo.load()

    while True:
        print("\n--- МЕНЮ ---")
        print("1. Додати співробітника")
        print("2. Видалити співробітника")
        print("3. Додати авто")
        print("4. Видалити авто")
        print("5. Додати продаж")
        print("6. Видалити продаж")
        print("7. Звіти")
        print("8. Зберегти дані")
        print("9. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            name = input("ПІБ: ")
            pos = input("Посада: ")
            phone = input("Телефон: ")
            email = input("Email: ")
            repo.add_employee(Employee(name, pos, phone, email))

        elif choice == "2":
            name = input("Введіть ПІБ співробітника для видалення: ")
            repo.remove_employee(name)

        elif choice == "3":
            manufacturer = input("Виробник: ")
            year = int(input("Рік: "))
            model = input("Модель: ")
            cost = float(input("Собівартість: "))
            sale = float(input("Ціна продажу: "))
            repo.add_car(Car(manufacturer, year, model, cost, sale))

        elif choice == "4":
            model = input("Введіть модель авто для видалення: ")
            repo.remove_car(model)

        elif choice == "5":
            if len(repo.employees) == 0 or len(repo.cars) == 0:
                print("Спершу додайте співробітників та авто!")
                continue
            emp_name = input("Введіть ПІБ продавця: ")
            employee = None
            for e in repo.employees:
                if e.full_name == emp_name:
                    employee = e
                    break
            if not employee:
                print("Співробітник не знайдений")
                continue
            car_model = input("Введіть модель авто: ")
            car = None
            for c in repo.cars:
                if c.model == car_model:
                    car = c
                    break
            if not car:
                print("Авто не знайдено")
                continue
            date = input("Дата продажу (YYYY-MM-DD): ")
            price = float(input("Реальна ціна продажу: "))
            repo.add_sale(Sale(employee, car, date, price))

        elif choice == "6":
            print(repo.list_sales())
            idx = int(input("Введіть номер продажу для видалення (з 0): "))
            repo.remove_sale(idx)

        elif choice == "7":
            print("\n--- ЗВІТИ ---")
            print("1. Усі співробітники")
            print("2. Усі авто")
            print("3. Усі продажі")
            print("4. Продажі співробітника")
            print("5. Найпопулярніший автомобіль за період")
            print("6. Найуспішніший продавець за період")
            print("7. Прибуток за період")

            r = input("Ваш вибір: ")
            report = ""

            if r == "1":
                report = repo.list_employees()
            elif r == "2":
                report = repo.list_cars()
            elif r == "3":
                report = repo.list_sales()
            elif r == "4":
                name = input("Введіть ПІБ: ")
                report = repo.all_sales_by_employee(name)
            elif r in ["5", "6", "7"]:
                start = datetime.strptime(input("Початкова дата (YYYY-MM-DD): "), "%Y-%m-%d")
                end = datetime.strptime(input("Кінцева дата (YYYY-MM-DD): "), "%Y-%m-%d")
                if r == "5":
                    report = "Найпопулярніший авто: " + repo.most_sold_car(start, end)
                elif r == "6":
                    report = "Найуспішніший продавець: " + repo.best_seller(start, end)
                elif r == "7":
                    report = f"Прибуток: {repo.total_profit(start, end)}"

            if report != "":
                print("\n1. Вивести на екран\n2. Зберегти у файл")
                out_choice = input("Ваш вибір: ")
                if out_choice == "1":
                    print(report)
                elif out_choice == "2":
                    f = open("report.txt", "w", encoding="utf-8")
                    f.write(report)
                    f.close()
                    print("Звіт збережено у report.txt")

        elif choice == "8":
            repo.save()
            print("Дані збережено")

        elif choice == "9":
            repo.save()
            break

        else:
            print("Невірний вибір")


if __name__ == "__main__":
    menu()
