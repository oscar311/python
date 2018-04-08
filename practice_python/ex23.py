pl = []

with open('one.txt') as f:
    line = f.readline()
    while line:
        pl.append(int(line))
        line = f.readline()

hl = []
with open('two.txt') as d:
    line = d.readline()
    while line:
        hl.append(int(line))
        line = d.readline()

ol = []
for elem in pl:
    if elem in hl:
        ol.append(elem)
        
print(ol)