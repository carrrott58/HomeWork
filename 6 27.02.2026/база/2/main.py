with open("24-263.txt") as file:
    f1=file.readline()

#способ 1
m=10000
for x in range (len(f1)):
    for y in range (x+m, x, -1):
        c= f1[x:y+1]
        if c.count("A")>=30:
            m=min(m, len(c))
        else:
            break
print(m)
