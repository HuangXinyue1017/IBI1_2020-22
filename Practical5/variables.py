a=171020
b=190784
c=100320
d=abs(a-c)
e=abs(a-b)
if (d>e):
	print("d is larger")
else:
	print("e is bigger")

X=True
Y=False
Z=(X and not Y)
print("Z=",Z)
W=(X!=Y)
print("W=",W)
print("Ans=",W==Z)