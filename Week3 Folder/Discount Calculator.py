while True:
    amount=float(input("Original amount: "))
    if amount<0:
        print("Amount should be greater than 0,Try again!")
    else:
        break

if amount<10000:
    discount=0
    
elif amount >=10000 and amount <50000:
    discount=5

else:
    discount=10

final_amount=amount-(amount*(discount/100))

#Output Section
print("Your Original amount is ",amount)
print("Your discount percentage is",discount,"%")
print("Final amount payable is",final_amount)
