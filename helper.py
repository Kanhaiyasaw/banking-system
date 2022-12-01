#this class is helper purpose like deposite, withdraw and show_balace  
class help:
    # for deposite calculation 
    def deposite(self):
        self.bal = 0
        self.dip_amt = input("Enter Amount for Deposite: ")
        self.bal = self.bal+int(self.dip_amt)
        print("depsite Successfully Complated : ", self.dip_amt + "/-")
        print("Your account balance Now:  ", self.bal) 

    #for withdraw calculation
    def withdraw(self):
        self.wt_amt = input("Enter Amount for withdraw: ")
        if self.bal >= int(self.wt_amt):
            self.bal = self.bal-int(self.wt_amt)
            print("withdrawal Successfully complated : ", self.wt_amt + "/-")
            print("")
        else:
            print("not enough balance in your A/c....Sorry")
        print("Your account balance Now:  ", self.bal)
    
    #for check balance
    def show_bal(self):
        print("Your account balance Now:  ", self.bal)