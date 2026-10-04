import random

a = ["rock","paper","scissor"]
b= (random.choice(a)).lower()
print("choices : \n 1.Rock \n 2.Paper \n 3.scissor\n")
i = (input("Enter your choise : ")).lower()




if( i != b):
    if(i == "rock"  and b=="scissor"):
        print("you win")
    elif(i == "rock" and b == "paper"):
        print("you lose")
    elif(i == "paper" and b=="scissor" ):
        print("you lose")
    elif(i == "paper" and b=="rock"):
        print("you win")
    elif(i == "scissor" and b=="rock"):
        print("You lose")
    elif(i == "scissor" and b=="paper"):
        print("You win")
else:
    print("You both give same input")


print("Cmputer input is : "+b)


    





    
    