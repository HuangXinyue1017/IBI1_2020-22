class Student(object):
	def __init__ (self,first_name,last_name,programme):
		self.first_name=first_name
		self.last_name=last_name
		self.programme=programme
	def describe(self):
		print('Full name:',self.first_name,self.last_name)
		print('Undergraduate programme:',self.programme)

A=Student('XY','H','BMI')
A.describe()