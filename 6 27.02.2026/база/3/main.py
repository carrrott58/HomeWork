with open("24-263.txt") as file:
    f1=file.readline()

#способ 1
m=1000
for x in range (len(f1)):
    for y in range (x+m, x, -1):
        c = f1[x:y+1]
        if c.count("X")<=80:
            if c.count("X")>=30:
                print(m)
                m=min(m, len(c))
        else:
            break
print(m)
