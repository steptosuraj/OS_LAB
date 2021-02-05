l=list(map(int,input("Enter initial list space separated : ").split()))
print(f"Entered list is : {l}")
while(1):
    choice=int(input("1:Insert at any position \n2:Append in list \n3:Delete from desired position \n4:exit\n "))
    if(choice==1):
        n=int(input("Enter number to be inserted : "))
        p=int(input("Enter position of number : "))
        l.insert(p-1,n)
        print(l)
    elif(choice==2):
        l.append(int(input("Enter number to be inserted : ")))
        print(l)
    elif(choice==3):
        x=int(input("Enter position of number to be deleted : "))
        del l[x-1]
        print(l)
    elif(choice==4):
        break
    else:
        print("Invalid Input")