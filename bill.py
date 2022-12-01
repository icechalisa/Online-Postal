class Bill:
    def __init__(self, user_name, cost):
        self.__user_name = user_name
        self.__cost = cost

    def create_bill(self, information, box):
        print(" ")
        print(" ")
        print("Online Postal".center(50))
        print("-----------------------------------------------")
        print("Receipt".center(50))
        print("-----------------------------------------------")
        print(f'Name: {self.__user_name}')
        print(" ")
        print("Receiver info")
        print(f'Name: {information["name"]}')
        print(f"Address: {information['address']}")
        print(f"Phone number: {information['phone']}")
        print("-----------------------------------------------")
        print("Description...                            price")
        total_price = 0
        for i in range(len(box)):
            print(f"Box size: {box[i]['size']}                        {box[i]['price']}")
            total_price += box[i]['price']
        print(f"Shipping rate:{self.__cost:>31}")
        print("-----------------------------------------------")
        print(f"Total:{total_price + self.__cost:>39}")
        print("-----------------------------------------------")
        print("Thank you for using our service!")
