# Enter your code here. Read input from STDIN. Print output to STDOUT
a = ".|."
x,y = map(int,input().split())
for e in range(1,int(x/2)+1):
    print(((a*((e*3)-(e+1))).center(y,'-')))
print("WELCOME".center(y,'-'))
for x in range(int(x/2),0,-1):
    print((a*((x*3)-(x+1))).center(y,'-'))
    

