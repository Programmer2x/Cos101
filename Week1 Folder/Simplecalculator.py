import random
score=0
print("Welcome to my calculator game")
while True:
    num1=random.randint(1,10)
    num2=random.randint(1,10)
    answer=float(input(f"{num1}*{num2} = "))


    if answer==num1 *num2:
        print ("correct")
        score+=1
        continue 
    else:
        print("Incorrect your score is ",score)
        break
        

    
    

