l=[]
sum=0
n=int(input("Enter total number count : "))
print("Enter numbers")
for _ in range(n):
    x=int(input())
    l.append(x)
    sum+=x
print("Entered numbers are : ")
for i in l:
    print(i,end=" ")
print()
print(f"Average : {sum/n}")