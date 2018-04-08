# Write a function that takes an ordered list of numbers (a list where the elements are in order from 
# smallest to largest) and another number. The function decides whether or not the given number is inside 
# the list and returns (then prints) an appropriate boolean.

def binarySearch(i_list, item):
    f = 0
    l = len(i_list)-1
    found = False
   

    while f <= l and not found:
        mp = (f+l)//2
        if i_list[mp] == item:
            found = True
            return found
        else:
            if int(item) < int(i_list[mp]):
                l = mp-1
            else:
                f = mp+1


    return found



def main():

    x = raw_input("Enter number: ")

    i_list = raw_input("Enter list: \n").split(",")

    print(i_list)

    i_list.sort()

    print(binarySearch(i_list,x))



main()