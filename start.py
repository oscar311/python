import sys

def main():
    print ("HEllo world!")
    i, j = 1, 0
    while i < 6:
        print (str(i) +" "+ str(j))
        i+=1
        j+=1

    print(sys.version)

# end function

main()

