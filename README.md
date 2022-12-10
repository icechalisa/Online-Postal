
Project title : Online Postal
Project overview and features
     The program is online postal. The user has to login before using, if the user already has an account 
which the username and password is correct, they will be able to access the application. 
And the user has to sign up if they don’t have the account. After login they have to fill in 
the information of the recipient and the package information as well. 
Then the user has to choose whether to register or express this package. 
At the end the program will calculate the price that must be paid and come out as a receipt
Required libraries and tools
    classes : class Account, class Package, class receiver, class bill
    Interact with user on the console. : ask user to fill in the package information.
    Read/write data from/to text files : read the account information from the text file and write the 
account information to the text file.
    GitHub URL : https://github.com/icechalisa/Online-Postal.git
new account which user had created into the text file.
Program design -- what are your classes are and what are their objectives
    Account class : contain function to check the account information and function to write the new account.
    Package class : store the information of the package and calculate the price.
    Receiver class : store the information of the receiver.
    Bill class : create the bill which contain the information of the package and the price.
Code structure -- how many source files and what each of them contains
    There are 4 source files. 
    The main.cpp file contains the main function and the function to check the account information.
    The account.cpp file contains the function to check the account information and function to write the new account.
    The package.cpp file contains the function to store the information of the package and calculate the price.
    The receiver.cpp file contains the function to store the information of the receiver.
    The bill.cpp file contains the function to create the bill which contain the information of the package and the price.
    

