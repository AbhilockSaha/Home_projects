w = input("Enter the word: ")
m = list("avijit")  # convert to list so we can modify characters
n = min(len(w), len(m))  # to avoid index errors

for i in range(n):
    if w[i] == m[i]:
        m[i] = w[i]

m = ''.join(m)  # convert list back to string
print("Result:", m)
