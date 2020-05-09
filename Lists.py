if __name__ == '__main__':
    N = int(input())
    listt = []
    for x in range(N):
        usercommand = input().split()
        if usercommand[0]=="insert":
            listt.insert(int(usercommand[1]),int(usercommand[2]))
        elif usercommand[0] == "print" :
            print(listt)
        elif usercommand[0]=="remove":
            listt.remove(int(usercommand[1]))
        elif usercommand[0]=="append":
            listt.append(int(usercommand[1]))
        elif usercommand[0]=="sort":
            listt.sort()
        elif usercommand[0]=="pop":
            listt.pop()
        elif usercommand[0]=="reverse":    
            listt.reverse()
        

