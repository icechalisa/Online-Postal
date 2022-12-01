class Receiver:
    def __init__(self):
        self.__name = None
        self.__address = None
        self.__phone_number = None
        self.__info = {}

    def fill_data(self):
        print("-----------------------------------------------")
        print("Please fill in the following information.")
        self.__name = input("Receiver name: ")
        self.__address = input("Receiver address: ")
        self.__phone_number = input("Receiver phone number: ")
        self.__info["name"] = self.__name
        self.__info["address"] = self.__address
        self.__info["phone"] = self.__phone_number
        return self.__info
