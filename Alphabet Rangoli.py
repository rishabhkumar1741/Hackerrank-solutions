def print_rangoli(size):
    letters = list(map(chr,range(97,122)))
    letters = "".join(letters)
    length = len("-".join(letters[0:size]))+len("-".join(letters[0:size])[1:]) 
    for x in range(size-1):
        a = "-".join(reversed(letters[size-1-x:size])).rjust(int(length/2)+1,'-')
        print(a,a[-2::-1],sep=(''))
    mainn = "-".join(list(reversed(letters[0:size])))
    print(mainn+mainn[-2::-1])
    for x in range(size-1):
        eve = "-".join(list(reversed(letters[x+1:size])))
        print(eve.rjust(int(length/2)+1,'-')+eve[-2::-1].ljust(int(length/2),'-'))
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)