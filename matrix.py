n = int(input("Enter the colom : "))
m = int(input("Entr the row : "))


arr1 = [[1,2,3],[4,5,6],[7,8,9]]
arr2 = [[1,2,3],[4,5,6],[7,8,9]]
for i in range (n):
    for j in range(m):

        arr1[i][j] = [arr1[i][j] * arr2[i][j]]
print(arr1)        