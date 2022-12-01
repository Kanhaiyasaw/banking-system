import random # for random number creation 
import time # for time managment
import helper as hp # for preform withdraw and diposite Operation
class cust:

    # public variables
    ac=random.randint(11111111111,99999999999) # a/c number creating
    pwd=random.randint(11111,99999) # password creating

    # In this function role is take deatil about user 
    #  account creation 
    # userid and password creation for login 
    def open_account(self):
            self.first_name = input("Enter your first name: ")
            self.last_name = input("Enter your Last name: ")
            self.DOB = input("Enter your Date Of Birth(dd/mm/yyyy): ")
            self.contact_num = input("Enter your Contact Number: ")
            print("creating Your Account.......")
            
            #from time pakage
            #it will wait 3.5 second
            time.sleep(3.5)  
            print("")
            print("Congratulation...")
            print("Your Account is Succesfully Created..")
            self.fullname = self.first_name + self.last_name

            #Account created here...
            print("Your Account Name is: ", self.fullname)
            print("your Account Number : ", cust.ac)
            print("")

            #Ask for userid and password
            c=input("You want login in to Bank Y : ")

            #if say yes 
            if c=='Y':
                print("your UserId: ", self.fullname)
                print("your Password: ", cust.pwd)
                #redirect in login_user method
                self.login_user()
            
            #other wise redirect bank class
            else:
               bank().__class__()
            
    #for show detail about A/C holder but this function not used anywhere
    def show_detail(self):
            print("First Name : ",self.first_name)
            print("Last Name : ",self.last_name)
            print("Date Of Birth : ",self.DOB)
            print("Contact Number : ",self.contact_num)

    #for login 
    # choose opration like withdraw, deposite and check balance
    def login_user(self):
        x = input("Enter UserId : ")
        y = input("Enter Password : ")
        print(cust.pwd)
        if x==self.fullname and y == str(cust.pwd):
            print("Welcome To our Bank ", self.fullname)
            print("what you want to perform...")
            print("***************Options*********************")
            print("1. withdraw")
            print("2. Deposite")
            print("3. check balance")
            print("4. Exit")
            print("*******************************************")
            print("")
            print("Enter You choice only from 1,2,3")
            self.choice=input() # record choice of user and response according to choice
            if self.choice == '1':
                hp.help.withdraw(self)
                self.login_user()
            elif self.choice == '2':
                hp.help.deposite(self)
                self.login_user()
            elif self.choice == '3':
                hp.help.show_bal(self)
                self.login_user()
            elif self.choice == '4':
                bank().__class__() 
            else:
                print("Enter Valid Option")
        else:
            print("------Wrong UserID and Password ------")
            print("Try Again....")
            self.login_user()

#this class use when new user are come into the program
# choose option here like account opening, login 
class bank(cust):

    # Initial state
    def __init__(self):
        print("***************Options*********************")
        print("1. Open Account")
        print("2. Login As a A/c Holder")
        print("3. Login As a Bank Manager")
        print("*******************************************")
        print("")
        print("Enter You choice only from 1,2,3")
        self.choice=input() # record choice of user and response according to choice
        if self.choice == '1':
            customer_obj=cust()
            customer_obj.open_account()
        elif self.choice == '2':
            print("Login Customer")
        elif self.choice == '3':
            print("login manager")
        else:
            print("Enter Valid Option")
   
#start all system by here calling this class
# calling bank class
exe = bank()
