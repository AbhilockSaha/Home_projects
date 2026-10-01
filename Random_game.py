import random 

x = random.randint(1,10)

print("\n---- Thank You For Playing This Game ----\n")

print("Enter how many chances you want :-")
choise = int(input())
count = 0
for i in range(choise):
    my_input = int(input("Your Input :- "))
    count +=1
    if my_input == x :
        print(f"You Won \nTotal Chances You Take {count}\nTotal Choice You Asked For{choise}")
        break
    elif(my_input < x):
        print("Your Input Is Less Than Value")
    elif(my_input > x):
        print("Your Input Is Greater Than Value")
    else:
        print("Try Agaiin")
print(f"Real Value Is {x}")