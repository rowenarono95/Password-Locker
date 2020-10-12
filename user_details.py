import random
import string

user = []
details = []

class Credentials:
    def __init__ (self, site_name, user_name, password):
        self.site_name = site_name
        self.user_name = user_name
        self.password = password


    def cred():
        print("Choose one of the following")
        print("n\ 1. Put in existing accounts n\ 2. Create new crediantials account n\ 3. View exisiting crediantaials")
        my_option = input()
        if my_option == "1":
            person1 = Credentials(site_name = input("Account Name: "), user_name = input("Username: "), password = input("Password: "))
            print(person1)
            details.append(person1)
        elif my_option == "2":
            print("Do you want an account generated password")
            print("n\ 1. Yes n\ 2. No")
            option = input()
            if option == "1":
                pass1 = User.password(10)
                person2 = Credentials(site_name = input("Account Name: "), user_name = input("Username: "), password = pass1)
                details.append(person2)
                for obj in details:
                    print(obj.site_name, obj.user_name, obj.password)
            elif option == "2":
                person1 = Credentials(site_name = input("Account Name: "), user_name = input("Username: "), password = input("Password: "))
                details.append(person1)
            else:         
                print("Invalid input")
        elif "3":
            for obj in details:
                print(obj)
        else:
            ("Invalid")

    

            
            



   


class User:
    def __init__ (self, first_name, second_name, password):
        self.first_name = first_name
        self.second_name = second_name
        self.password = password

    def login():
        print("KIndly repeat your details to login")
        # firstname = input("Firstname: ")
        # secondname = input("Secondname: ")
        # password1 = input("Password: ")
        Credentials.cred()
        # for obj in user:
        #     print(obj)

        # if obj.firstname == first_name and obj.secondname == second_name and obj.password1 == password:
        #     print("twendelee")
        # else:
        #     print("Matata")


    def signup():
        user1 = User(input("Firstname: "), input("Secondname: "), input ("Password: "))
        user.append("user1")
        User.login()

    def password(length):
        letters = string.ascii_lowercase
        result = ''.join(random.choice(letters) for i in range(10))
        return result

    







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





