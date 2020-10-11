print("Hello, welcome! ")
print("Choose one of the following: lg for login, su for signup and exit for ex")
option = input()

if option == "lg":
    print("Kindly login")
elif option == "su":
    print("Kindly signup")
elif option == "ex":
    exit()
else:
    print("invalid")

class User:
    def __init__ (self, first_name, second_name, password):
        self.first_name = first_name
        self.second_name = second_name
        self.password = password




class Credentials:
    pass

