b = 9
for i in range(1, 7):
    if i == 1 or i == 4:

        print((' *' * i).rjust(b, ' '))
    else:
        print('    * ', '   ', ' *')
    b += 1
    print()
