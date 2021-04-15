import re
import string

# Create class Student
class Student(object):
	def __init__ (self,first_name,last_name,programme):
		self.first_name=first_name
		self.last_name=last_name
		self.programme=programme
	def describe(self):
		print('Full name:',self.first_name,self.last_name)
		print('Undergraduate programme:',self.programme)

line=input("Please input the first name, last name, and programme of the student:",)
line=line.strip()
line=line.split()
A=Student(line[0],line[1],line[2])
A.describe()