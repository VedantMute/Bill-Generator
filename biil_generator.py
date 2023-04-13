#  BILL GENERATOR APPLICATION LIKE PROGRAM WHICH GENERATES BILL FOR GIVE ITEMS IN PROPER FORMATTED MANNER
#  ©️ VEDANT MUTE




from datetime import date, datetime
now = datetime.now()

item=["vadapav","samosa","poha","water"]
price=[15,15,20,10]

f=open("bill_Data.txt","w")
f.write("            SNACKS CENTER             \n")
f.write("______________________________________\n")
f.write("Bill No-                              \n")
f.write("Date-")
f.write(str(now.strftime("%Y-%m-%d %H:%M:%S")))
f.write("\n")
f.write("______________________________________\n")
f.write("item              Qty            Total\n")
f.write("______________________________________\n")


def menu():
    print("select option\n") 
    print("1. vada pav\n")
    print("2. samosa\n")
    print("3. poha\n")
    print("4. water\n")
    print("0. exit\n")
    print("7. options\n")

def evaluate(o,q,v):
    f.write(item[o-1])
    f.write("\t\t\t  ")
    f.write(str(q))
    f.write("\t\t\t\t  ")
    f.write(str(v))
    f.write("\n")

def calculate(opt):
    #  match opt:
    #         case 1:
    #             value = price[opt] * quantity
    #             evaluate(option,quantity,value)
    #         case 2:
    #             value = 15 * quantity
    #             evaluate(option,quantity,value)
    #         case 3:
    #             value = 20 * quantity
    #             evaluate(option,quantity,value)
    #         case 4:
    #             value = 10 * quantity
    #             evaluate(option,quantity,value)
    if opt != 0:
        value=price[opt-1]*quantity
        evaluate(option,quantity,value)
    return value                



total=0

while True:
    
    menu()
    option=int(input("enter option: "))
    if option==0:
        break
 
    quantity=int(input("enter quantity:")) 
    
    finalValue=calculate(option)
    
    total=total+finalValue
f.write("\n______________________________________")
f.write("\nTotal			              	  ")
f.write(str(total))
f.write("\n______________________________________")
