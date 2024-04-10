balance=0
def deposit(amount):
    global balance
    balance+=amount
    print(f"After deposit balance is {balance}") 
def withdraw(amount):
    global balance
    if balance<amount:
        print("Insufficient balance")
    else:
        balance-=amount
        print(f"After withdraw balance is {balance}")
def checkbalance():
    return balance
while True:
   try: 
    print("ATM services")       
    print("1.deposit")
    print("2.withdraw")
    print("3.balance")
    print("4.Exit")
    ch=int(input("Read your choice:"))
    if ch==1:
        amt=int(input("Enter the amount:"))
        if amt<=0:
            print("Invalid | Re-enter")
        else:    
            deposit(amt)
    elif ch==2:
        amt=int(input("Enter the amount:"))
        if amt<=0:
            print("Invalid | Re-enter")
        else:
            withdraw(amt)    
    elif ch==3:        
        print("Available Balance",checkbalancebalance())
    elif ch==4:
        print("Thank you ")
        break 
   except:
       print("Invalid input ! Enter some thing")      