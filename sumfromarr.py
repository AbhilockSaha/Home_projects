l = [12,5,4,1,9,7,8,6,5]

number = 10
for i in range(len(l)):
    for j in range(i+1,len(l)):
        ans = l[i] + l[j]
        if(number == ans):
            print(l[i],l[j])