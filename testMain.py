val = None
with open("university.txt", 'r') as file:
    val = [line.rsplit() for line in file.readlines()]

print(type(val))
for item in val:
    print(item)