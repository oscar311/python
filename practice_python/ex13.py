# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them

def fib(x):

    if x < 2:
        return x
    else:
        return fib(x - 1) + fib(x - 2)

n = int(raw_input("Enter a number: "))

i = 1
while i <= n:
    print(str(fib(i)))
    i+=1
