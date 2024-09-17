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
loginAttempts = 0       #i was reset to 0 after each incorrect login attempt, causing i never to go above 3, same with transerTimes
transferTimes  = 0      #created "loginAttempts and globaled transferTimes to fix"


def get_password_from_username(username):         #added function to ease the burden of login()
    if username == '123':
        return user1.password
    else:
        return user2.password
    
def deposit(amount):
        user.bankValue = amount + user.bankValue
        print(f"New Bank Value: {user.bankValue}")

def withdraw(amount):
    if amount > user.bankValue:
        print("Bank balance is lower than attempted withdrawl amount, please try again.")
    else:
        user.bankValue = user.bankValue - amount
        print(f"New Bank Value: {user.bankValue}")

def transfer(ID, amount):
    global transferTimes

    if transferTimes < 3:
        if amount > user.bankValue:
            print("Bank balance is lower than attempted tranfser amount, please try again.") #changed transer to transfer
        else:
            user.bankValue = user.bankValue - amount
            transferTimes = transferTimes + 1
    
            if ID == 123:
                user1.bankValue = user1.bankValue + amount
                print(f"Your New Bank Value: {user.bankValue}")
            elif ID == 456:
                user2.bankValue = user2.bankValue + amount
                print(f"Your New Bank Value: {user.bankValue}")
            else:
                print("You entered an invalid ID to transfer to, please try again")
    else:
        print("You have reached your limit on transfers, please try again later")

def login():                                           #shortened login function
    while True:
        print('Please enter your ID number.')
        global user
        global loginAttempts

        inputUsername = input()

        if inputUsername == '123' or inputUsername == '456':
            print('Please enter your password.')
            passwordInput = input()                        #Removed Semicolon, changed i to loginAttempts for better readability
            if loginAttempts < 3:                          #Globaled loginAttempts so it doesn't get reset to 0
                if passwordInput == get_password_from_username(inputUsername):
                    print('Success, logged in.')
                    user = user1
                    break
                else:
                    print('Password incorrect, try again.')
                    loginAttempts = loginAttempts + 1
            else:
                print('Too many incorrect login attempts.')
                sys.exit()                             #changed break to sys.exit, otherwise program would continue even though password attempts were up
        else:
            print('Invalid, please enter a valid ID number.')

def main():                                            #added main function
    login()

    while True:                                        #cleaned up loop by using new functions
        print('Please enter the function you want to use: "Check Balance", "Deposit", "Withdraw", "Transfer", or "Log out".')

        userInput = input()

        if userInput == 'Check Balance':
            print(user.bankValue)
        elif userInput == 'Deposit':
            userInput = int(input('Enter the amount to deposit\n'))
            deposit(userInput)
        elif userInput == 'Withdraw':
            userInput = int(input('Enter the amount to withdraw\n'))
            withdraw(userInput)
        elif userInput == 'Transfer':
            userTransferId = int(input('Enter the user ID to transfer to\n'))
            amountTransfer = int(input('Enter the amount to transfer\n'))
            transfer(userTransferId, amountTransfer)      
        elif userInput == 'STOP':
            print('Bye.')
            break
        elif userInput == 'Log out':
            login()
        else:
            print('Invalid, please enter a valid function.')

if __name__ == "__main__":
    main()