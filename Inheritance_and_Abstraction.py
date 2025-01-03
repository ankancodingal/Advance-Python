#----------------Employee Details-------------------
# # parent class
# class Person( object ):	

# 		# __init__ is known as the constructor		
# 		def __init__(self, name, idnumber):
# 				self.name = name
# 				self.idnumber = idnumber
# 		def display(self):
# 				print(self.name)
# 				print(self.idnumber)

# # child class
# class Employee( Person ):		
# 		def __init__(self, name, idnumber, salary, post):
# 				self.salary = salary
# 				self.post = post

# 				# invoking the __init__ of the parent class
# 				Person.__init__(self, name, idnumber)

				
# # creation of an object variable or an instance
# a = Employee('Penguin', 20210401, 15000, "Intern")	

# # calling a function of the class Person using its instance
# a.display()

#----------------Student Details-------------------
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

# x = Student("Joey", "King", 2021)
# x.printname()
# print(x.graduationyear)

#----------------Animal Class-------------------
# # import necessary packages
# from abc import ABC, abstractmethod
# # create a base class
# class Animal(ABC):

#     # abstract method
# 	# should be implemented by all sub-classes
# 	def move(self):
# 		pass

# # sub classes
# class Human(Animal):

# 	def move(self):
# 		print("I can walk and run")

# class Snake(Animal):

# 	def move(self):
# 		print("I can crawl")

# class Dog(Animal):

# 	def move(self):
# 		print("I can bark")

# class Lion(Animal):

# 	def move(self):
# 		print("I can roar")
		
# # Driver code
# R = Human()
# R.move()

# K = Snake()
# K.move()

# R = Dog()
# R.move()

# K = Lion()
# K.move()




