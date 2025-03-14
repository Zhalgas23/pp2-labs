import math
import time

#1
def multiply_list(numbers):
    return math.prod(numbers)

#nums = list(map(int, input("Numbers: ").split()))
#result = multiply_list(nums)
#print("The product of all the numbers: ", result)

#2
def count_case(text):
    upper = sum(1 for char in text if char.isupper())
    lower = sum(1 for char in text if char.islower())

    print("Uppercase: ", upper)
    print("Lowercase: ", lower)

#user_text = input("String: ")
#count_case(user_text)

#3
def palindrome_check():
    string = input()


    if string == string[::-1]:

        print("It is a palindrome")
    else:
        print("It is not a palindrome")


#palindrome_check()

#4
def square_root():
    number = int(input("Number: "))
    delay = int(input("Delay: "))

    time.sleep(delay / 1000)

    result = math.sqrt(number)
    print("Square root of ", number, "after ", delay, "miliseconds is ", result)

#square_root()

#5
def all_true():
    my_tuple = tuple(map(eval, input("tuple elements: ").split()))

    result = all(my_tuple)

    print("All elements are True:", result)

#all_true()