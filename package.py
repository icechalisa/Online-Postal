class Package:
    def __init__(self):
        self.__box_size = None
        self.__weight = None
        self.__length = None
        self.__width = None
        self.__height = None
        self.__volume = 0
        self.__lst = []
        self.__box = []

    def size_is(self, rounds):
        for i in range(rounds):
            print(" ")
            print("Please fill in the package information")
            print("-----------------------------------------------")
            while True:
                try:
                    while True:
                        self.__weight = int(input("weight(kg):                       "))
                        if self.__weight <= 0:
                            print("Please enter a positive number.")
                        else:
                            self.__length = int(input("length(cm):                       "))
                            if self.__length <= 0:
                                print("Please enter a positive number.")
                            else:
                                self.__width = int(input("width(cm):                        "))
                                if self.__width <= 0:
                                    print("Please enter a positive number.")
                                else:
                                    self.__height = int(input("height(cm):                       "))
                                    if self.__height <= 0:
                                        print("Please enter a positive number.")
                                    else:
                                        break
                except ValueError:
                    print("Please fill in the information correctly.")
                else:
                    self.__volume = self.__width * self.__length * self.__height
                    print(f"volume(cm**3) is {self.__volume}")
                    print("-----------------------------------------------")
                    form = {'weight': self.__weight, 'volume': self.__volume}
                    self.__lst.append(form)
                    break
        return self.__lst

    def check_size(self):
        for i in range(len(self.__lst)):
            if self.__lst[i]['weight'] <= 5 or self.__lst[i]['volume'] <= 200:
                self.__box_size = "Small box"
                price = 30
            elif 10 >= self.__lst[i]['weight'] > 5 or 300 >= self.__lst[i]['volume'] > 200:
                self.__box_size = "Medium box"
                price = 60
            else:
                self.__box_size = "Large box"
                price = 100
            form = {'size': self.__box_size, 'price': price}
            self.__box.append(form)
        return self.__box

    def to_send(self):
        print("How would you like to ship your package?")
        while True:
            choice = input("1.Regular(20Baht)  2.Express(40Bath): ")
            if choice == "1":
                print("Your package will go by regular post...")
                return 20
            elif choice == "2":
                print("Your package will go by express post...")
                return 40
            else:
                print("Error, please try again.")
