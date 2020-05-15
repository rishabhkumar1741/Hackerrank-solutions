def count_substring(string, sub_string):
    count = 0
    for x in range(len(string)):
        if len(string[x:])>=len(sub_string):
            if string[x]==sub_string[0]:
                a = string[x:x+len(sub_string)]
                if a==sub_string :
                    count +=1        
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)