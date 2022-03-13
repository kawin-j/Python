# name: Jimmy Kawinseksan
# ID: 6010210329
# programme: find a prime numbers
num = int(input('Enter number: '))
i = 0
prime = []
while i < num:
    i += 1
    if i < 2:
        continue
    else:
        if i > 2 and (i%2 == 0):  # check all of even number except 2
            continue
        else:
            if i > 3 and i%3 ==0:  # skip all numbers have 3 as composite
                continue
            else:
                if i > 5 and i%5 ==0:  # skip all numbers have 5 as composite
                    continue
                else:
                    if i > 7 and i%7 == 0:  # skip all numbers have 7 as composite
                        continue
                    else:
                        prime.append(i)  # add all number that return false in the list
print(*prime, '\b', sep=',', end=' are prime numbers.')  # unpack the list following commas as seperator, the last comma was deleted.
