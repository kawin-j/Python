# name: Jimmy Kawinseksan
# ID: 6010210329
# programme: find total result between lower and higher numbers
lower_num = int(input('Enter lower number: '))
higher_num = int(input('Enter higher number: '))
result = 0
for i in range(lower_num, higher_num + 1):
    result += i
print("Result of calculation = ", result)
