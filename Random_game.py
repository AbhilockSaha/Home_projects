import random 

x = random.randint(1,10)

print("\n---- Thank You For Playing This Game ----\n")

print("Enter how many chances you want :-")
choise = int(input())
count = 0
for i in range(choise):
    my_input = int(input("Your Input :- "))
    count +=1
    if my_input == choise :
        print(f"You Won \n Total Chances You Take {count}")
    elif():
        print("Try again")