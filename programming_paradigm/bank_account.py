class BankAccount:
   
    def __init__(self , account_balance = 0  ):
        self.account_balance  =  account_balance 
    
    def deposit(self , amount) :
        self.account_balance += amount 

    def withdraw(self , amount) :

        if(self.account_balance >= amount ) : 
            self.account_balance -= amount
            return True 
        else :
            return False 

    def display_balance(self) :
        disp = self.account_balance
        print(f"Current Balance: ${disp:.2f}")


# bank_account =  BankAccount()
# bank_account.deposit(88)
# bank_account.withdraw(88)

# bank_account.display_balance()
 