file = open("c:/Users/Admin/Documents/readingwriting-files/Teams.txt","r+")

teams = ['dave', 'john', 'dai', 'tim', 'jim']


for n in teams:
    newline = n + '\n'
    file.write(newline)
    continue

file.seek(0)

print(file.readline())

print(file.readline())

file.close()

print('--------------------------------')

file = open("c:/Users/Admin/Documents/readingwriting-files/Teams.txt","r+")

outfile = ''
for line in range(1, 6):
    outfile += file.readline()

file.close()

file = open("c:/Users/Admin/Documents/readingwriting-files/Teams.txt","w")

file.write('new line\n')

file.write(outfile)

file.close()

file = open("c:/Users/Admin/Documents/readingwriting-files/Teams.txt","r+")

print(file.read())

print('test')
