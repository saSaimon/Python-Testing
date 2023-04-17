file = open('test.txt')

# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()
for line in file.readlines():
    print(line)
file.close()

