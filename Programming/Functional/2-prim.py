print(2)
s=[]
for i in range(3,1000):
    for j in range(2,i):
        if((i%j)==0):
            break
    else:
        s.append(i)

for i in s:
    if(str(i)==str(i)[::-1]):
        print(i)
