#----------------Class Student-------------------
# class student:
# 	grade = 10
# 	print("Hi I am a student of grade", grade)

# ob = student()

#----------------Class Student - II-------------------
# class student:
# 	grade = 10
# 	name = "Penguin"
	
# 	def introduction(self):
# 		print("Hi I am a student")

# 	def details(self):
# 		print("My name is", self.name)
# 		print("I study in Grade", self.grade)

# ob = student()
# ob.introduction()
# ob.details()


#----------------Parrot Bird-------------------
# class Parrot:

#     # class attribute
#     species = "bird"

#     # instance attribute
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# # instantiate the Parrot class
# blu = Parrot("Blu", 10)
# woo = Parrot("Woo", 15)

# # access the class attributes
# print("Blu is a {}".format(blu.species))
# print("Woo is also a {}".format(woo.species))

# # access the instance attributes
# print("{} is {} years old".format( blu.name, blu.age))
# print("{} is {} years old".format( woo.name, woo.age))


#----------------Parrot Bird - II-------------------
# class Parrot:
    
#     # instance attributes
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     # instance method
#     def sing(self, song):
#         return "{} sings {}".format(self.name, song)

#     def dance(self):
#         return "{} is now dancing".format(self.name)

# # instantiate the object
# blu = Parrot("Blu", 10)

# # call our instance methods
# print(blu.sing("'Happy'"))
# print(blu.dance())


#----------------Robot Introduction-------------------
# import pygame
# import sys

# # Initialize Pygame
# pygame.init()

# # Screen settings
# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption('Simple Robot Simulation')

# # Colors
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)

# # Robot settings
# robot_pos = [400, 300]
# robot_size = 50
# robot_speed = 5

# # Main loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         robot_pos[0] -= robot_speed
#     if keys[pygame.K_RIGHT]:
#         robot_pos[0] += robot_speed
#     if keys[pygame.K_UP]:
#         robot_pos[1] -= robot_speed
#     if keys[pygame.K_DOWN]:
#         robot_pos[1] += robot_speed

#     # Clear screen
#     screen.fill(WHITE)

#     # Draw robot (a simple rectangle)
#     pygame.draw.rect(screen, RED, (*robot_pos, robot_size, robot_size))

#     # Update display
#     pygame.display.flip()

#     # Cap the frame rate
#     pygame.time.Clock().tick(30)

