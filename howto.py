space = "\n"
print("Hello World")

print("   /|")
print("  / |")
print(" /  |")
print("/___|")
print(space)
character_name = "Mike"
character_age= "50"
is_Male= False
print("There once was a man named " + character_name + ",")
print("he was " + character_age + " years old")

character_name = "Tommy"
print("He really liked the name " + character_name + ",")
print("but didn't like being " + character_age + ".")

phrase = "Giraffe Academy"


print(phrase + " is cool!")
print("Using the addition sign to add things with strings")
print(space)

print(phrase.upper() .isupper())
print ("Making things uppercase and true and falsing it")
print(space)

print(len(phrase))
print("Checking the length of a string")
print(space)

print(phrase[3])
print("Using the square bracket to find a certain character with the corrensponding number\n(a phrase always start with zero)")
print(space)

print(phrase.index("G"))
print("Using the index to find the corrensponding number with the character.")
print(space)

print(phrase.index ("Academy"))
print("Using the index to find the corrensponding number with the word.")
print ("\n")

print(phrase.replace("Giraffe", "Elephant"))
print("Using the replace function to replace words.")
print (space)

print( 3 * (4 + 5 ))
print("Using numbers for math")
print (space)

print(10%3)
print(space)

from math import *

my_num = -4049166203
print(str(my_num) + " my favorite number")
print(space)
print("Using string function to combine phrases and words ")
print(space)

print(abs(my_num))
print("Using the absolute function to find the absolute number")
print(space)

print(pow(3, 2))
print("Using the power function to put numbers against the power of another number.")
print(space)

print(max (3, 2))
print("Max function tells you which of the two numbers are bigger")
print(space)

print(min (3, 2))
print("Min function tells you which of the two numbers are smaller")
print(space)

print(round(3.2))
print(round(3.7))
print("The round function rounds up the decimal to nearest whole number.")
print(space)

print(floor(3.7))
print("Floor function looks for the lowest number \n"
      "essentially chopping off the decimal point")
print(space)

print(sqrt(36))
print("The sqrt function returns the number back to the square root.")
print(space)

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name+ "! You are " + age +"!" )
print(space)

print("The int function makes the variables into intergers \n"
      "aka a whole number.")
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2)

print(result)
print(space)

print("The float function makes it to that you can use decimals as well as whole numbers")
num1 = input("Enter a number: (Use a decimal) ")
num2 = input("Enter another number: (Use another decimal) ")
result1= float(num1) + float(num2)

print(result1)
print(space)

color= input("Enter a color: ")
plural_noun= input("Enter a plural noun: ")
celebrity= input("Enter a celebrity: ")


print("Roses are " + color)
print(plural_noun +  " are blue")
print("I love "+ celebrity +  "!")
print(space)

print("Whenever you use square brackets \n "
      "python recognizes that you making a list of values")
friends = ["Myles", "Jasmine", "Asher", "Meghan", "Morgan", "Bobby"]
print("As for the index of names"
      "Myles = 0 \n"
      "Jasmine = 1 \n"
      "Asher = 2 \n"
      "Meghan = 3 \n"
      "Morgan = 4 \n"
      "Bobby = 5 \n"
      "Negative numbers start with the number 1 when indexing \n"
      "negative numbers also start from the back of the list"
      "Myles = -6"
      "Jasmine = -5"
      "Asher = -4"
      "Meghan = -3"
      "Morgan = -2"
      "Bobby = -1")
print(friends [0])
print (friends[-1])

print(space)
print("Using a colon following the number you want to start with \n"
      "allows you to only display the list that you want and whatever is after that. ")
print(friends [3:])
print(space)

print("Using the number, colon =, \n "
      "then another number would then create a range of the numbers from the list")
print (friends [3:5])
print(space)

print("Even with this you can change your variables \n"
      " without changing the entire list")
friends[3] = "Rumay"
print(friends [3:5])
print(space)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Myles", "Jasmine", "Asher", "Meghan", "Morgan", "Bobby"]
friends.extend(lucky_numbers)
print(friends)
print(space)

friends.append("Creed")
print(friends)
print(space)

friends.insert(1, "Rumay")
print(friends)
print(space)

friends.remove ("Bobby")
print(friends)
print(space)

friends.clear
print(friends)
print(space)

friends.pop()
print(friends)
print(space)

print(friends.index ("Meghan"))


