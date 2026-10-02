def factor(n):
    x = []

    for i in range(2,n+1):

        while n%i == 0 and n > 0:
            x.append(i)

            n = n//i

    return x

if __name__ == "__main__":    
    n = 600851475143
    ans = factor(n)
    for x in ans:
        print(x, end=' ')
