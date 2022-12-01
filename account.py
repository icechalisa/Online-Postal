import json


class Account:
    def __init__(self):
        self.__user_name = None
        self.__password = None

    def login(self):
        print("Welcome to Online Postal Service".center(50, "-"))
        ask = input("Do you have an account with us?(y,n) ")
        if ask == "y":
            print('LOGIN'.center(50, "-"))
            with open('account.json', mode='r') as data_file:
                data = json.load(data_file)
            while True:
                self.__user_name = input("Please enter your username: ")
                if self.__user_name in data:
                    while True:
                        self.__password = input("Please enter your password: ")
                        if data[self.__user_name] == self.__password:
                            print(f"...Welcome back {self.__user_name}...")
                            break
                        else:
                            print("Error, please try again.")
                    break
                else:
                    print("Please retry again.")
        elif ask == "n":
            with open('account.json', mode='r') as data_file:
                data = json.load(data_file)
            while True:
                user_ = input('Please enter your username: ')
                if user_ in data:
                    print("You already have an account, please try again")

                else:
                    passw_ = input('Please enter your password: ')
                    data[user_] = passw_
                    with open('account.json', mode='w') as data_file:
                        json.dump(data, data_file, indent=4)
                    print('Please confirm your username and password')
                    while True:
                        self.__user_name = input("Please enter your username: ")
                        if self.__user_name in data:
                            while True:
                                self.__password = input("Please enter your password: ")
                                if data[self.__user_name] == self.__password:
                                    print(f"...Welcome {self.__user_name}...")
                                    break
                                else:
                                    print("Error, please try again.")
                            break
                        else:
                            print("Please retry again.")
                    break
        return self.__user_name
