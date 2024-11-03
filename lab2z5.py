
#a
with open('notowania_gieldowe.txt', 'r') as plik:
    for line in plik:
        print(line)


#b
with open("notowania_gieldowe.txt", "a") as plik:
      plik.write('ALR, 113\n')
with open('notowania_gieldowe.txt', 'r') as plik:
    for line in plik:
        print(line)