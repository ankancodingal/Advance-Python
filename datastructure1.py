#----------------Activity 1-------------------
# lst = ['Apple', 'Guava', 'Mango', 'Banana', 'Kiwi']

# print("Length of list:", len(lst))
# print("First Element:", lst[0])
# print("Last Element:", lst[-1])

# lst.append('Papaya')
# print("Updated List :", lst)

# lst.remove('Guava')
# print("Updated List :", lst)

# lst.sort()
# print("Sorted List:", lst)

# lst.pop(1)
# print("Updated List :", lst)

# lst.reverse()
# print("Reversed List :", lst)

# print("Multiplication on List :", lst*2)

# lst = lst[:4]
# print("Sliced List :", lst)

# lst.clear()
# print("Updated List :", lst)

#----------------Activity 2-------------------
# # empty dictionary
# my_dict = {}

# # dictionary with integer keys
# my_dict = {1: 'apple', 2: 'ball'}

# # dictionary with mixed keys
# my_dict = {'name': 'John', 1: [2, 4, 3]}

# my_dict = {'name': 'Jack', 'age': 26}

# # Output: Jack
# print(my_dict['name'])
# print(my_dict.get('age'))

# # update value
# my_dict['age'] = 27
# print(my_dict)

# # add item
# my_dict['address'] = 'Downtown'
# print(my_dict)

# # remove particular element
# my_dict.pop('age')
# print(my_dict)

# # access a particular element
# print("Address :", my_dict.get('address'))

# # remove all the elements
# my_dict.clear()
# print(my_dict)

#----------------Activity 3-------------------
# def test(lst):
# 	result = {}
# 	for item in lst:
# 		result[item[0]] = item[1:]
# 	return result

# students = [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]

# print("\nOriginal list of lists:")
# print(students)
# print("\nConverted  lists to a dictionary:")
# print(test(students))

#----------------ACP-------------------
# import random

# lower_bound = 1
# upper_bound = 5
# max_attempts = 12
# secret_number = random.randint(lower_bound, upper_bound)

# def get_guess():
#     while True:
#         guess = int(input("Guess a number between 1 and 5: "))
#         if lower_bound <= guess <= upper_bound:
#             return guess
#         else:
#             print("Invalid input. Please enter a number within the specified range.")

# def check_guess(guess, secret_number):
#     if guess == secret_number:
#       return "Correct"
#     elif guess < secret_number:
#         return "Too low"
#     else:
#         return "Too high"

# def play_game():
#     attempts = 0
#     won = False

#     while attempts < max_attempts:
#         attempts += 1
#         guess = get_guess()
#         result = check_guess(guess, secret_number)
#         if result == "Correct":
#             print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
#             won = True
#             break
#         else:
#             print(f"{result}. Try again!")
#     if not won:
#         print(f"Sorry, you ran out of attempts! The secret number is {secret_number}.")

# if __name__ == "__main__":
#     print("Welcome to the Number Guessing Game!")
#     play_game()


