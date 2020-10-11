user = []

class User:
    def __init__ (self, first_name, second_name, password):
        self.first_name = first_name
        self.second_name = second_name
        self.password = password

    def login():
        firstname = input("Firstname: ")
        secondname = input("Secondname: ")
        password1 = input("Password: ")
        Credentials.cred()
        for obj in user:
            print(obj)

        if obj.firstname == first_name and obj.secondname == second_name and obj.password1 == password:
            print("twendelee")
        else:
            print("Matata")


    def signup():
        user1 = User(input("Firstname: "), input("Secondname: "), input ("Password: "))
        user.append("user1")
        User.login()

    







print("Hello, welcome! ")
print("Choose one of the following: lg for login, su for signup and ex for exit")
option = input()

if option == "lg":
    print("Kindly login")
elif option == "su":
    User.signup()
elif option == "ex":
    exit()
else:
    print("invalid")


class Credentials:
    def __init__ (self, first_name, second_name, password):
        self.first_name = first_name
        self.second_name = second_name
        self.password = password
    print("")

