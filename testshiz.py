list = [2, 2, 2, 8, 8, 8]
list2 = []
count = 0
while count <= len(list):
    if list[count] == 8:
        list2.append(list.pop(count))
    count += 1
print(list)
print(list2)

