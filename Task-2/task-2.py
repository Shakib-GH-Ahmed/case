inp=open("input2.txt","r")
out=open("output2.txt","w")

run=inp.readline().strip()
run=int(run)
lst=inp.readline().split()

for i in range(run):
    tag=False
    for j in range(run-i-1):
        if int(lst[j]) > int(lst[j+1]):
            lst[j],lst[j+1] = lst[j+1],lst[j]
            tag=True
    if tag==False:
        break
    
for i in range(run):
    if i==len(lst)-1:
        out.write(f"{lst[i]}")
    else:
        out.write(f"{lst[i]} ")

inp.close()
out.close()

#In the best case, we have to look for the first iteration when it terminates. (when i=0)
# So, I used a variable tag, which initially holds the value false. (tag=False)
# If any swapping has been done in the first iteration, the tag will turn into true, but if not, it will remain false.
# Since there is no swapping done in the first iteration, the list is already sorted, and I break the loop with the condition that the tag is false.