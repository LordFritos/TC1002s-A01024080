#io_utilities
import numpy as np

class Student():
	def __init__(self,name,lastName,major):
		self.name = name
		self.lastName = lastName
		self.major = major
		self.grades = []
	def addGrade(self,grade):
		self.grades.append(grade)
		print("A grade of {} was added to the student {} {}".format(grade,self.lastName,self.name))
	def getAverage(self):
		return np.mean(self.grades)


def studentCheck():
	edo = Student("Miguel","Frias","IM")

	print(edo.major)
	print(edo.grades)

	edo.addGrade(95)
	edo.addGrade(100)
	edo.addGrade(85)

	print(edo.grades)

	average = edo.getAverage()
	print("The average is {}".format(average))

if __name__ == "__main__":
	studentCheck()

