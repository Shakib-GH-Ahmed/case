inp=open("input1b.txt","r")
out=open("output1b.txt","w")

test=inp.readline().strip()
test=int(test)
for i in range(test):
    lst=inp.readline().strip().split(" ")
    if lst[2] == "+":
        out.write(f'The result of {lst[1]} + {lst[3]} is {int(lst[1]) + int(lst[3])}\n')
    elif lst[2] == "-":
        out.write(f'The result of {lst[1]} - {lst[3]} is {int(lst[1]) - int(lst[3])}\n')
    elif lst[2] == "*":
        out.write(f'The result of {lst[1]} * {lst[3]} is {int(lst[1]) * int(lst[3])}\n')
    elif lst[2] == "/":
        out.write(f'The result of {lst[1]} / {lst[3]} is {int(lst[1]) / int(lst[3])}\n')

inp.close()
out.close()