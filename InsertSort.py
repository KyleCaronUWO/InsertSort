## Insertion Sort Script
## Created by Kyle Caron

ls = [9, 2, 7, 48, 59, 71, 1]

length = len(ls)
for index in range(1, length):
    insertindx = index
    current = ls.pop(index)
    for next in range(index-1, -1, -1):
        if ls[next] > current:
            insertindx = next
    ls.insert(insertindx, current)

print(ls)