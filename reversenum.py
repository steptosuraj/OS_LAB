n=int(input("Enter number to be reversed : "))
sum=0
remainder=0
while n>0:
    remainder=n%10
    sum=sum*10+remainder
    n=n//10
print(f"Reversed number is {sum}")