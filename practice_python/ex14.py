# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.

names = raw_input("Enter sentence: \n").split(" ")

i = len(names) -1

r_names = []

while i != 0:
    r_names.append(names[i])
    i-=1

print(r_names)
