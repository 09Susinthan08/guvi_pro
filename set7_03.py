# your code goes here
q=input()
w=""
li=[]
for i in range(0,len(q)):
    if q[i] not in w:
        w=w+q[i]
    elif q[i] in w :
        li.append(len(w))
        w=""
    if i==len(q)-1:
        li.append(len(w))
        w=""
    
print(max(li))
