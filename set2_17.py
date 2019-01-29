# your code goes here
a,b=map(int,input().split(" "))
flag=0
li=list(map(int,input().split(" ")))
for i in range(len(li)):
	for j in range(i+1,len(li)):
		if(li[i]+li[j]==b):
			print("yes")
			flag=1
		else:
			continue
if(flag==0):
	print("no")
