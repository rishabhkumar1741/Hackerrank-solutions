if __name__ == '__main__':
    listt = []
    marks = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        listt += [[name,score]]
        marks.append(score)
    lastsecondmarks = list(sorted(set(marks)))
    listt.sort()
    for x ,n in listt:
        if lastsecondmarks[1] == n:
            print(x)