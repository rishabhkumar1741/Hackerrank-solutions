def print_formatted(number):
    eve= len(str(bin(number))[2:])
    for x in range(1,number+1,1):
        print("{} {} {} {}".format(str(x).rjust(eve),oct(x)[2:].rjust(eve),hex(x)[2:].rjust(eve).upper(),bin(x)[2:].rjust(eve)))
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)