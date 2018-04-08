# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.


i = int(raw_input("Enter the divisor "))

nums = range(1,1001)

for e in nums:
    if e % i == 0:
        print(str(e) + " has a divisor "+str(i))