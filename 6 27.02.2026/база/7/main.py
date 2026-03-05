with open("24_14_1715944482.txt") as file:
    f1=file.readline()

#способ 1
m=10000
for x in range (len(f1)):
    for y in range (x+m, x, -1):
        c= f1[x:y+1]
        if c.count("E")>=240:
            m=min(m, len(c))
        else:
            break
print(m)
