if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))
"""
Reason why we hash() function in python
https://stackoverflow.com/questions/17585730/what-does-hash-do-in-python
"""