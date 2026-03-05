from re import *

with open('bI4DufyyF.txt') as file:
    f1 = file.readline()


num = r'([789][0789]*)'
expression = fr'({num}\*)*0(\*{num})*'
expression = fr'{expression}(\-{expression})*'
reg = fr'{expression}(\-{expression})*'
# reg = fr'(?=({expression}))'
m = max([x.group() for x in finditer(reg,f1)], key=len)
print(len(m), m)