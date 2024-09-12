# How to Use
When program is started, a message will display prompting the user to input their ID number, specifying that you can type "STOP" at any time to close the program.

# Hardcoded users to use:
ID: 123  
Password: Password1  
Starting Bank Value: $300  

ID: 456  
Password: Password2  
Starting Bank Value: $500  

# Actions

Check Balance: once logged in to an account, type "Check Balance" to print out the current bank value associated with that account.  
Deposit: type "Deposit" and then enter the amount of money to add to the account. New total will be displayed before bringing you back to the menu page.  
Withdraw: type "Withdraw" and then enter the amount of money to take out, there will be a check that at least that amount of money is in the account.  
Transfer: type "Transfer" to transfer money, you will be prompted to enter the ID of the account to transfer to, and then the amoung of money to be transfered.  

# Functional Requirements
1. sign in to a users account with a password linked to it, and with a dollar amount associated with the account    
2. deposit and withdraw money from that account  
3. transfer money between two distinct accounts

# Non-Functional Requirements
1. be unable to withdraw more than is in the account
2. only be able to transfer 3 times from an account

# Design Constraints
1. Language must be python
