days=int(input("Number of days: "))
total=0
days_greater=0
days_less=0

while days<=0:
    print("Number of days cannot be 0 or negative")
    days=int(input("Number of days: "))
else:
    for i in range(days):
        i+=1
        sales=float(input(f"Sales for day {i}: " ))
        if sales<0:
            print("Sales cannot be negative")
            sales=float(input(f"Sales for day {i}: "))
        elif sales>=10000:
            total+=sales
            days_greater+=1
            pass
        
        elif sales<10000:
            total+=sales
            days_less+=1
            pass

#Process
average=total/i


#Output        
print("Total Sales: NGN",total)
print("Average Daily sales:",average)
print("Days with sales of at least NGN 10,000:",days_greater)
print("Days with sales below NGN 10,000:",days_less)
