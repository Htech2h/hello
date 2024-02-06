lis = [2,4,5,1]
target = 5

x = 0
y = 0

result = []

while True:
    if lis[x] + lis[y] == target:
        result.append(lis.index(lis[x]))
        result.append(lis.index(lis[y]))
        break
    y += 1
    if y == len(lis):
        x += 1
        y = 0

print(result)