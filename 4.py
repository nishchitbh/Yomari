from copy import deepcopy

a = [[1, 1], [2, 2], [3, 3]]
counts = []
for i in a:
    b = deepcopy(a)
    b.remove(i)
    slopes = []
    count = 1
    for j in b:
        try:
            slope = (i[1] - j[1]) / (i[0] - j[0])
        except:
            slope = 20
        slopes.append(slope)
    liscounter = []
    for z in slopes:
        liscounter.append(slopes.count(z))
    counts.append(max(liscounter))
print(max(counts) + 1)
