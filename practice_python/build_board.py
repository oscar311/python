from __future__ import print_function



def build_board(x):
    str1 = " ---"
    str2 = "|   "

    i = 0
    while i < x:
        h = 0
        while h < x:

            
            print(str1 , end='')
            h+=1

        j = 0
            
        print()

        while j < x:
            print(str2, end='')
            j+=1

        print(str2)

        i+=1



    if x%2 != 0:
        h = 0
        while h < x:

            
            print(str1 , end='')
            h+=1

            
        print()


i = raw_input("Enter n: ")

build_board(int(i))