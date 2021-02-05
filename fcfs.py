process=[]
avg_wt=0
avg_tat=0

n=int(input("Enter no of process: "))
for i in range(n):
	process.append([])
	process[i].append(int(input("Enter pid: ")))
	process[i].append(int(input("Enter arrival time: ")))
	process[i].append(int(input("Enter burst time: ")))
	print (' ')
process.sort(key = lambda process:process[1])

ctime=process[0][1]
print ('pid\t\tarrival\t\tburst\t\tcompletion\tturn-around\twaiting')
for i in range(n):
    ctime+=process[i][2]
    tat=ctime-process[i][1]
    wt=tat-process[i][2]
    avg_wt+=wt
    avg_tat+=tat
    print (process[i][0],'\t\t',process[i][1],'\t\t',process[i][2],'\t\t',ctime,'\t\t',tat,'\t\t',wt)
print(f"Average waiting Time : {avg_wt/n}")
print(f"Average Turn-Around Time : {avg_tat/n}")