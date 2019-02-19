# your code goes here
q=int(input())
li=[]
for i in range(q):
	li1=list(map(int,input().split()))
	li.extend(li1)
li.sort()
print(*li)
