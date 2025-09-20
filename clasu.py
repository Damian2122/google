from uuid import uuid4

class User:
    def __init__(self, login):
        print("we create object classs")
        self.login = login
        strId = str(uuid4())
        self.password = strId [0:8]
        print(f"U password = <{self.password}>. Save this!!!")
        self.age = 0
        self.name = ""
        self.address = ""
        self.region = ""
        self.phone = ""

    def print_auth_info(self):
        print(f"U info L {self.login}\tPass = {self.password}")

    def info(self):
        print(f"Name = {self.name}\tage = {self.age}\tPhone = {self.phone}\tAddress = {self.address}\tRegion = {self.region}")

    def change_password(self):
        old_password = input("Enter old password: ")
        if old_password == self.password:
            new_pass = input("Enter new password: ")

            # джпт написав
            if len(new_pass) < 8:
                print("Пароль має містити не менше 8 символів!")
                return
            if not any(c.isupper() for c in new_pass):
                print("Пароль має містити хоча б одну велику літеру!")
                return
            if not any(c.isdigit() for c in new_pass):
                print("Пароль має містити хоча б одну цифру!")
                return
            # тут вже не джпт писав

            self.password = new_pass
        else :
            print("Wrong password")



    def create_profile(self):
        self.name = input("Enter your name: ")
        self.address = input("Enter your address: ")
        self.phone = input("Enter your phone: ")
        self.age = input("Enter your age: ")
        self.region = input("Enter your region: ")

print("Welcome to app!!!")
u1 = User("admin")

while True:
    anw = input("Enter command: ")
    if anw == "exit":
        break
    elif anw == "1":
        u1.print_auth_info()
    elif anw == "2":
        u1.create_profile()
    elif anw == "3":
        u1.info()
    elif anw == "4":
        u1.change_password()

    else:
        print("""Wrong command! Look what we can do:
        1 - Print_auth_info
        2 - Create profile
        3 - Info
        4 - Change password""")
