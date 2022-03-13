# name: Jimmy Kawinseksan
# ID: 6010210329
# programme: calculate result from conversion of string '1'  by determining a number of '1'
given_num = int(input('Input number: '))
accord_string = ''
i = 0
according_num = 0
while i < given_num:
    i += 1
    accord_string = accord_string + '1'
    according_num += int(accord_string)
print(according_num)
