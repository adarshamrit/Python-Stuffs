
a = int(input("Enter a number"))

sum = 0

while a>0:
    n = a%10
    sum=sum+n
    a=a//10
print("Sum of the digits is:", sum)
