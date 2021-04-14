import re

# Create class Student
class Student(object):
	def __init__ (self,first_name,last_name,programme):
		self.first_name=first_name
		self.last_name=last_name
		self.programme=programme
	def describe(self):
		print('Full name:',self.first_name,self.last_name)
		print('Undergraduate programme:',self.programme)

# The example name list is in student.txt
f=open('students.txt','r')

for line in f.readlines():
	line=line.strip()
	line=line.split()
	A=Student(line[0],line[1],line[2])
	A.describe()

f.close()