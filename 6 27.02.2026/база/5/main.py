with open("24-208.txt") as file:
    f1=file.readline()

#способ 1
m=0
for x in range (len(f1)):
    for y in range (x+m, len(f1)):
        c= f1[x:y+1]
        if c.count("2022")<=4:
            m=max(m, len(c))
        else:
            break
print(m)
