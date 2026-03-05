with open("kQTF43F8B.txt") as file:
    f1=file.readline()

#способ 1
m=0
for x in range (160, len(f1)):
    for y in range (x+m, len(f1)):
        c= f1[x:y+1]
        if c.count("CD")<=160:
            if c.count("CD")==160:
                print(m)
                m=max(m, len(c))
        else:
            break
print(m)
