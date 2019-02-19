# your code goes here
a1,b1=map(int,input().split())
a2,b2=map(int,input().split())
a3,b3=map(int,input().split())
a4,b4=map(int,input().split())
q=b2-b1
w=b3-b4
e=a3-a2
r=a4-a1
if q==w and e==r:
	print("yes")
else:
	print("no")
