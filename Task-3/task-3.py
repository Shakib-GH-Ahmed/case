inp=open("input3.txt","r")
out=open("output3.txt","w")

run=inp.readline().strip()
run=int(run)
lst1=inp.readline().split()
lst2=inp.readline().split()
com_lst=[]
for num in range(run):
    com_lst.append([int(lst1[num]),int(lst2[num])])
for i in range(run):
    c=i
    for j in range(i+1,run):
        if com_lst[j][1] > com_lst[c][1]:
            c=j
        elif com_lst[j][1] == com_lst[c][1]:
            if com_lst[j][0] < com_lst[c][0]:
                c=j
    com_lst[i],com_lst[c]=com_lst[c],com_lst[i]
    
for idx in range(len(com_lst)):
    if idx==len(com_lst)-1:
        out.write(f"ID: {com_lst[idx][0]} Mark: {com_lst[idx][1]}")
    else:
        out.write(f"ID: {com_lst[idx][0]} Mark: {com_lst[idx][1]}\n")

inp.close()
out.close()