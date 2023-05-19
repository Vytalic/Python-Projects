# Ben Clarkdefinition
# CSCI II 161 L03
# Assignment 8


MenuLoop = 1

### Begin account class definition
class Account:
    def __init___(self):
        self.name = '<userInput>'
        self.savings = float(100)
        self.checking = float(20)
        self.card = float(10)
        self.limit = int(50)
### End account class definition
  
### Begin Menu function definition      
def menu():
    global MenuLoop
    while MenuLoop != 3:
        print("***********************************************")
        print('Option 1: Display Balance')
        print('Option 2: Cash Services')
        print('Option 3: Exit')
        print("***********************************************\n")
        userInput = int(input("Enter '1' to DISPLAY BALANCE, '2' for CASH SERVICES, or '3' to EXIT: "))
        print()
        
        if userInput == 1:
            displayBalance()
        elif userInput == 2:
            cashServices()
        elif userInput == 3:
            MenuLoop = input("Are you sure you want to exit? y/n: ")
            if MenuLoop == 'y':
                MenuLoop = 3
            else:
                MenuLoop = 1
### End Menu function definition

#### Display-balance function definition
def displayBalance():
    balSav = account1.savings
    availSav = account1.savings + 10
    if account1.checking >= 0:
        balCheck = account1.checking
        availCheck = account1.checking
    else:
        balCheck = "$0"
        availCheck = "$0"
    balCard = account1.card
    availCard = account1.limit - account1.card
    
    print('[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]\n')
    print('                         Account Owner: ', account1.name, '\n')
    table1 = [
        ['       ', 'Account', 'Balance    ', '|', 'Available', 'Balance']
             ]
    for row in table1:
        print("{: ^15} {: ^7} {: ^12} {: ^3} {: ^9} {: ^7}".format(*row))
    table2 = [
        ['Savings', '$', balSav, '|', '$', availSav],
        ['Checking', '$', balCheck, '|', '$', availCheck],
        ['Card', '$', balCard, '|', '$', availCard]
             ]
    for row in table2:
        print("{: ^15} {: ^7} {: ^12.2f} {: ^3} {: ^8} {: ^8.2f}".format(*row))
    print('\n[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]\n')   
#### End balance function definition

#### Begin cash-services function definition
def cashServices():
    bool2 = 0
    while bool2 == 0:
        print('            -----------------------------------------------------------------------')
        print('            |||||||||||||    "S" - Savings     |    "K" - Checking    |||||||||||||')
        print('            -----------------------------------------------------------------------\n')
        accountType, depositAmount = input('Please specify the ACCOUNT TYPE and TOTAL AMOUNT you would like to deposit. (Example: K 200): ').split()
        accountType = accountType.upper()
        if accountType == 'S':
            account1.savings += int(depositAmount)
            print('\n$',depositAmount, 'has been deposited into the SAVINGS account.\n')
            bool2 += 1
        elif accountType == 'K':
            account1.checking += int(depositAmount)
            print('\n$',depositAmount, 'has been deposited into the CHECKING account.\n')
            bool2 += 1
        else:
            print('You have typed something incorrectly. Press "enter" and try again ... carefully.')
            print('You have typed something incorrectly. Press "enter" and try again ... carefully.')
            input('You have typed something incorrectly. Press "enter" and try again ... carefully.')

#### End cash-services function definition
  
  
#### Main program execution defined below
account1 = Account()

print("\nHello!\n")
account1.name = input("To begin, type your name and press enter: ")
account1.savings = 100.00
account1.checking = 20.00
account1.card = 10.00
account1.limit = 50.00
welcomeName = account1.name + '!'
print("\n                 Welcome,", welcomeName, "\n")

menu()