from datetime  import date, datetime

name=input("enter your name:")

# list of items:
lists='''
      Salt           40/kg
      Coffie Powder  80/each
      Sugar          60/kg
      Maggi          30/kg
      Oil            20/liter
      Soaps          50/each
      Rice           80/kg
      Ice Cream      70/each
                              '''


# declartion:

price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]
# Rates for items:
items={"Salt":40,
       "Coffie Powder":80,
       "Maggi":30,"Oil":20,"Soaps":50,"Rice":80,"Ice Cream":70}
option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=float(input("if you want to buy press 3 or 4 for exit:"))
    if inp1==4:
        break
    if inp1==3:
        item=input("Enter your items:")
        quantity=float(input("Enter your quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,items,quantity,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sry you entered item is not available")
    else:
        print("you enter wrong number")
    inp=input('are u want to bill the items yes or no:')
    if inp=="yes":
        pass
        if finalamount!=0:
            print(25*"=","sruthi supermarket",25*"=")
            print(30*" ","penukuduru")
            print("Name:",name,30*" ","Date:",date.today())
            print(74*"-")
            print("sno",7*" ","items",7*" ","quantity",7*" ","price")
            for i in range(len(pricelist)):
                print(i, 7*' ',7*' ',ilist[i],5*' ',qlist[i],plist[i])
            print(74*"-")
            print(50*" ","Total price",'Rs',totalprice)
            print("gst amount:",50*" ",'Rs',gst)
            print(74*"-")
            print(50*" ","final amount",'Rs',finalamount)
            print(74*"-") 
            print(50*" ","thanks for visiting")  
            print(74*"-") 