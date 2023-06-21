inp=open("input1a.txt","r")
out=open("output1a.txt","w")

test=inp.readline().strip()
test=int(test)
for i in range(test):
    next=int(inp.readline().strip())
    if next % 2 == 0:
        out.write("Even\n")
    else:
        out.write("Odd\n")
        
inp.close()
out.close()