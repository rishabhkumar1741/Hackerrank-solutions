def swap_case(s):
    mai = ""
    for x in range(len(s)):
        if s[x]==" ":
            mai+=s[x]
        elif  True == s[x].isupper():
            mai+=s[x].lower()
        else:
            mai+=s[x].upper()
    return mai

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)