#Ask user for number that forms a multiplicatio table from 1 to 12
#Number cannot be less than 1 and then reject those values

while True:
    num=int(input("Number: "))
    while num <1:
            print("Error, the value should be greater than 0")
            num=int(input("Number: "))

    for i in range(1,13):
        result=num * i
        print(f"{num} * {i} = {result}")

    end=input("Press E to end or any number to continue")
    if end=="E":
        break
    elif end.isdigit():
        pass
    
