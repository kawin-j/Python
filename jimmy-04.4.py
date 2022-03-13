# name: Jimmy Kawinseksan 
# ID: 6010210329
# programme: Numeric pattern
n = int(input("Number of pattern: "))
k = 1
for i in range(1, n):
    for j in range(1, n):
        print(k, end=" ")
        k += 1
    print()
