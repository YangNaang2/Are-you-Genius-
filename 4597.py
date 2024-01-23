a = input()
while True:
    if a == "#":
        break
    else:
        c = 0
        for i in range(0, len(a)-1):
            if a[i] == "1":  
                c += 1
        if a[-1] == "e":
            if c % 2 == 0:
                a = a[:-1] + "0"
            else:
                a = a[:-1] + "1"
        elif a[-1] == "o":
            if c % 2 == 0:
                a = a[:-1] + "1"  
            else:
                a = a[:-1] + "0"
        print(a)
        a = input()
