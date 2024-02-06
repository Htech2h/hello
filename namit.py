x = input("neme: ")

w = -1

while True:
    print(x[w] , end="")
    w -= 1
    if abs(w) > len(x):
        break

