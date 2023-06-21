inp=open("input4.txt","r")
out=open("output4.txt","w")

run=inp.readline().strip()
run=int(run)
store=[]
for i in range(run):
    lst=inp.readline().split()
    store.append([lst[0],lst[4],lst[6]])
for i in range(run):
    for j in range(i+1,run):
        if store[i][0] > store[j][0]:
            store[i],store[j]=store[j],store[i]
        elif store[i][0] == store[j][0]:
            if store[j][2] > store[i][2]:
                store[i],store[j]=store[j],store[i]
for i in range(run):
    if i == run-1:
        out.write(f"{store[i][0]} will departure for {store[i][1]} at {store[i][2]}")
    else:
        out.write(f"{store[i][0]} will departure for {store[i][1]} at {store[i][2]}\n")
    
inp.close()
out.close()