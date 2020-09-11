space= "\n"
#Whenever you use square brackets python recognizes that you making a list of values
friends = ["Myles", "Jasmine", "Asher", "Meghan", "Morgan", "Bobby"]
print("As for the index of names"
      "Myles = 0 \n"
      "Jasmine = 1 \n"
      "Asher = 2 \n"
      "Meghan = 3 \n"
      "Morgan = 4 \n"
      "Bobby = 5 \n"
#(Negative numbers start with the number 1 when indexing negative numbers also start from the back of the list "Myles = -6" "Jasmine = -5" "Asher = -4" "Meghan = -3" "Morgan = -2" "Bobby = -1"

print(friends [0])
print (friends[-1])

print(space)
#Using a colon following the number you want to start with allows you to only display the list that you want and whatever is after that.
print(friends [3:])
print(space)

#Using the number, colon =, \n " "then another number would then create a range of the numbers from the list
print (friends [3:5])
print(space)

#Even with this you can change your variables without changing the entire list
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
