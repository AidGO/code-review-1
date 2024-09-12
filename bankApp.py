import sys

print('Welcome to the Bank App! To close the program, simply enter "STOP" at any time, to begin:')

class User1:
    id = 123
    bankValue = 300
    password = 'Password1'

class User2:
    id = 456
    bankValue = 500
    password = 'Password2'

user = ""
user1 = User1
user2 = User2

def login():
    while True:
        print('Please enter your ID number.')
        global user

        userInput = input()

        if userInput == '123':
            print('Please enter your password.')
            userInput = input()
            i = 0;
            if i < 3:
                if userInput == user1.password:
                    print('Success, logged in.')
                    user = user1
                    break
                else:
                    print('Password incorrect, try again.')
                    i = i + 1
            else:
                print('Too many incorrect login attempts.')
                break
        elif userInput == '456':
            print('Please enter your password.')
            userInput = input()
            i = 0;
            if i < 3:
                if userInput == user2.password:
                    print('Success, logged in.')
                    user = user2
                    break
                else:
                    print('Password incorrect, try again.')
                    i = i + 1
            else:
                print('Too many incorrect login attempts.')
                break
        else:
            print('Invalid, please enter a valid ID number.')

login()

while True: 
    print('Please enter the function you want to use: "Check Balance", "Deposit", "Withdraw", "Transfer", or "Log out".')

    userInput = input()

    if userInput == 'Check Balance':
        print(user.bankValue)
    elif userInput == 'Deposit':
        print('Enter the amount to deposit')
        userInput = int(input())
        user.bankValue = userInput + user.bankValue
        print(f"New Bank Value: {user.bankValue}")
    elif userInput == 'Withdraw':
        print('Enter the amount to withdraw.')
        userInput = int(input())

        if userInput > user.bankValue:
            print("Bank balance is lower than attempted withdrawl amount, please try again.")
        else:
            user.bankValue = userInput - user.bankValue
            print(f"New Bank Value: {user.bankValue}")
    elif userInput == 'Transfer':
        transferTimes = 0

        print('Enter the user ID to transfer to.')
        userTransferId = int(input())
        print('Enter the amount to transfer.')
        amountTransfer = int(input())

        if transferTimes < 3:
            if amountTransfer > user.bankValue:
                print("Bank balance is lower than attempted transer amount, please try again.")
            else:
                user.bankValue = user.bankValue - amountTransfer
                transferTimes = transferTimes + 1
        
                if userTransferId == 123:
                    user1.bankValue = user1.bankValue + amountTransfer
                    print(f"Your New Bank Value: {user.bankValue}")
                elif userTransferId == 456:
                    user2.bankValue = user2.bankValue + amountTransfer
                    print(f"Your New Bank Value: {user.bankValue}")
                else:
                    print("You entered an invalid ID to transfer to, please try again")
        else:
            print("You have reached your limit on transfers, please try again later")


    
                  
    elif userInput == 'STOP':
        print('Bye.')
        break
    elif userInput == 'Log out':
        login()
    else:
        print('Invalid, please enter a valid function.')
