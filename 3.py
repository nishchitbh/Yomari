a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [[]]
for i in a[::-1]:
    count = 0
    for j in i:
        result[count].append(j)
        # print(result)
        count += 1
        result.append([])
print(result[0:len(a)])
"""a = [1, 1, 2, 3, 4, 2, 2, 3, 3]
a.
print(a)"""
