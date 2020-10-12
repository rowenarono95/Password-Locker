import random
import string

user = []
details = []

class Credentials:
    def __init__ (self, site_name, username, password):
        self.site_name = site_name
        self.username = user_name
        self.password = password

    def password(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(10))

    def cred():
        print("Choose one of the following")
        print("n\ 1. Put in existing accounts n\ 2. Create new crediantials account n\ 3. View exisiting crediantaials")
        my_option = input()
        if my_option == "1":
            person1 = input("Account Name: "), input("Username: "), input("Password: ")
            print(person1)
            details.append(person1)
        elif my_option == "2":
            print("Do you want an account generated password")
            print("n\1. Yes n\2. No")
            option = input()
            if option == "1":
                person2 = (input("Account Name: "), input("Username: "), result_str)
                details.append("person2")
                print(person2)
            else:
                print("it's never that serious")
        elif "3":
            print("Hold up")
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





