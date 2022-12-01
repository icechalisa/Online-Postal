from account import Account
from package import Package
from bill import Bill
from receiver import Receiver

ac = Account()
user = ac.login()

pk = Package()
while True:
    try:
        piece = int(input("How many package do you want to send?: "))
    except ValueError:
        print("Only number in this information!")
    else:
        find = pk.size_is(piece)
        break
box = pk.check_size()
cost = pk.to_send()

rec = Receiver()
information = rec.fill_data()

b = Bill(user, cost)
b.create_bill(information, box)
