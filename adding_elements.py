alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(alpha)

#append(): Adds an item to the end of the list.

val=input("Enter a value to append: ")
alpha.append(val)

print(alpha)

print("After append:")
for i in alpha:
    print(i, end=' ')
print("")
#insert(): Inserts an item at a specified index.

val=input("Enter a value to insert: ")
index=int(input("Enter the index to insert at: "))
alpha.insert(index, val)

print(alpha)

print("After insert:")
for i in alpha:
    print(i, end=' ')
print("")
#extend(): Adds elements from an iterable (e.g., another list) to the end of the list.

val=input("Enter a list of values to extend with (comma-separated): ")
new_elements = val.split(",")
alpha.extend(new_elements)

print(alpha)

print("After extend:")
for i in alpha:
    print(i, end=' ')
print("")