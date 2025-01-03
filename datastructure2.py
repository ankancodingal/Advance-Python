#----------------Operations on Tuple-------------------
# # Empty tuple
# my_tuple = ()
# print(my_tuple)

# # Tuple having integers
# my_tuple = (1, 2, 3)
# print(my_tuple)

# # tuple with mixed datatypes
# my_tuple = (1, "Hello", 3.4)
# print(my_tuple)

# # nested tuple
# my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
# print(my_tuple)

# # Accessing tuple elements using indexing
# my_tuple = ('p','e','r','m','i','t')
# print(my_tuple[0])   
# print(my_tuple[5])   

# # nested tuple
# n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# # nested index
# print(n_tuple[0][3])       
# print(n_tuple[1][1])      

# # Slicing
# print("Sliced :", my_tuple[1:4])

# # Iterating through tuple
# for letter in (my_tuple):
#     print("Hello", letter)


#----------------Operations on Set-------------------
# my_set = {1,2,2,3,4,4,4}
# print("Set :", my_set)

# my_set.add(5)
# print("Updated Set:", my_set)

# set1 = my_set
# set2 = {2,4,4,6}

# print("\nSet 1", set1)
# print("Set 2", set2)
# print("Difference")
# print(set1.difference(set2))
# print("Symmeteric Difference")
# print(set1.symmetric_difference(set2))

#----------------Set Union-------------------
# setc1 = {"green", "blue"}
# setc2 = {"blue", "yellow"}
# print("Original sets:")
# print(setc1)
# print(setc2)
# setc = setc1.union(setc2)
# print("\nUnion of above sets:")
# print(setc)

#----------------Set Intersection-------------------
# setx = {"green", "blue"}
# sety = {"blue", "yellow"}
# print("Original set elements:")
# print(setx)
# print(sety)
# print("\nIntersection of two said sets:")
# setz = setx.intersection(sety)
# print(setz)

#----------------Tuple to List-------------------
# # Define a tuple
# GFG_tuple = (1, 2, 3)

# # Convert the tuple to a list
# GFG_list = list(GFG_tuple)
# print(GFG_list)



