number = int(input("Enter the number : "))
length = len(str(number))
o = number
ans =0
for i in range(length):
    temp = number %10
    re = int(number /10)
    # print(temp)
    ans += (temp**3)
    number = re
    
    
if(o == ans):
    print(f"{o} is armstrong ")
else:
    print(f"{o} is not armstrong ")