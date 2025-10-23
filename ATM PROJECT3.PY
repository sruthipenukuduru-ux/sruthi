# ATM
s='''credit
      debit
      mini statement
      exit'''
Amount=2000
name="sruthi"
password="9491"
user_name=input("enter the user_name:")
passwords=input("enter the password:")
if name==user_name and password==passwords:
    print(s)
    while True:
        option=int(input("enter the option:"))
        if option==1:
            credit_amount=float(input("entet the amount:"))
            print("Amount after credit:",Amount+credit_amount)
        elif option==2:
              debit_amount=float(input("entet the amount:"))
              print("amount after debit:",Amount+debit_amount)
        elif option==3:
              print("###mini statementamount :",Amount)
        elif option==4:
          break
else:
  print("incorrect amount")