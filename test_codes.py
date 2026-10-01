# name = input("Enter your name: ")
# age = input("Enter your age: ")

# print(f"Hello, {name}! Next year, you will be {int(age) + 1} years old.")


# celcius = input("Enter temperature in Celsius: ")

# fahrenheit = (float(celcius) * 9/5) + 32

# print(f"{celcius} celcius is {fahrenheit} in fahrenheit.")

# digit = int(input("Enter a number to create a muliplication table: "))


# num = int(input("input a number to see if it is even or odd: "))

# if (num % 2 == 0):
#     print("yep it is an even number")
# elif (num % 3 == 0):
#     print("it's an odd number")
# else:
#     print("invalid bro!! come on")

# num = int(input("input a number: "))

# if num > 0:
#     print("the number is positive")
# elif num < 0:
#     print("nope negative bro")
# elif num == 0:
#     print("engk it's zero")
# else:
#     print("Invalid")


# year = int(input("input a calendar year: "))

# if year % 4 == 0 and year % 400 == 0:
#     print("leap year yey")
# else:
#     print("not leap year")


# grade = int(input("Input a grade and i will tell you your mark: "))

# if grade >= 70:
#     print("A")
# elif grade >= 60 and grade <= 69:
#     print("B")
# elif grade >= 50 and grade <= 59:
#     print("C")
# elif grade >= 40 and grade <= 49:
#     print("D")
# elif grade < 40:
#     print("F")

# for i in range(1, 11):
#     product = digit * i
#     print(f"{i} * {digit} = {product}")


# for i in range (1, 31):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     else:
#         print(i)


# text = input("Please provide a name to be reverse: ")

# print(text.lower()[::-1])


# word = input("Please provide a Word: ")

# vowels = "aeiou"

# total = 0

# for i in word.lower():
#     if i in vowels:
#         total += 1

# print(f"The total vowels in the word {word} is {total}")


# def palindrome(test):
#     reverse = test.lower()[::-1]

#     if test == reverse:
#         print("it is a palindrome yey!!")
#     else:
#         print("nope. not palindrome dude")


# word = input("test for palindrome: ")

# palindrome(word)

import random

while True:
    secret_number = random.randint(1, 100)
    print(secret_number)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Please enter a whole number.")
            continue


        if guess > 100:
            print("Bruh, I said 1 to 100")
            continue

        attempts += 1

        if guess > secret_number:
            print("Lower!")
        if attempts == 7:
            print(f"you lose....Game over!! the number is {secret_number}")
            break
        elif guess < secret_number:
            print("Higher!")
        else:
            print(f"Correct! The number was {secret_number}.")
            print(f"You got it in {attempts} attempts.")
            break

    choice = input("Do you want to play again? (y/n): ")
    if choice != "y":
        print("Thanks for playing!!")
        break
