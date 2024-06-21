# Your solution to Exercise 8
n=int(input("Enter a number: "))
for i in range (2,n+1):
    if i%2==1:
        continue
    print(i,end=" ")
print()