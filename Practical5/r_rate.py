#The number of IBI1 students
#The infection rate
#The time
n=84
r=1.1
t=0

#Start
while(t<5):
	n=n*(1+r)
	print(n)
	t+=1
