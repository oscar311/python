# Write a program that store the first 10 numbers that are divisable by 7 into a the variable called div_7.

def main():

    i = 0
    j = 0
    div_7 = []
    while j < 10:
        
        i+=1

        if i % 7 == 0:
            div_7.append(i)
            j+=1


    print div_7
# end function

main() 