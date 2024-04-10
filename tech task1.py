def celsius_to_fahrenheit(cel):
    fah=(cel*(9/5))+32
    return fah
def fahrenheit_to_celsius(fah):   
    cel=(fah-32)*(5/9)
    return cel
while True:
   try :
    print("Temperature Conversion")   
    print("1.celsius to Fahrenheit")
    print("2. Fahrenheit to celsius")
    print("3.Exit")
    ch=int(input("Read your choice:"))
    if ch==1:
        cel=float(input("Enter the Celsius temperature:"))
        result=celsius_to_fahrenheit(cel)
        print(f"After conversation to Fahrenheit the temperature is {result}")
    elif ch==2:
       fah=float(input("Enter the Fahrenheit temperature:"))
       result=fahrenheit_to_celsius(fah)
       print(f"After conversation to Celsius the temperature is {result}")     
    elif ch==3:
        print("Thank you")   
        exit(0)
    else:
        print("Invalid choice! Re-enter the choice") 
   except Exception:
    print("Enter any choice")           