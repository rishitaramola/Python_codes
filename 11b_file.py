#Question: Read from alpha.txt and num.txt, and print the contents.

#Read from alpha.txt
num=[]
alpha=[]
f=open('alpha.txt','r')
i=f.read()
for val in i.split():
    if val.isalpha():
        alpha.append(val)
    elif val.isdigit():
        num.append(int(val))
    else:
        pass
print("\nAlphabetical values:", alpha)
print("Numerical values:", num)

#write in file:
g=open('num.txt','w')

for val in num:
    g.write(str(val)+" ")
g.close()

#using f.tell and f.seek
f=open('alpha.txt','r')

print("\nFile name:", f.name)
print("File mode:", f.mode)
print("File closed:", f.closed)
print("Current position:", f.tell())
f.seek(0)
print("After seeking to beginning:", f.tell())
f.seek(5)
print("After seeking to 5:", f.tell())
f.close()
print("File closed:", f.closed)

with open('num.txt', 'r') as g:
    print("\nContents of num.txt:")
    print(g.read())

"""
f.seek(offset,whence)
    -whence can take values 0,1,2 standing for (0: beginning, 1: current position, 2: end)
"""
#Example:

f = open('alpha.txt', 'r')

f.seek(0)
print("\nAfter seeking to beginning:", f.tell())

f.seek(12, 0)
print("After seeking to 12:", f.tell())

# nonzero end-relative seek not allowed in text mode
f.seek(0, 2)          # move to end
print("End of file position:", f.tell())

# instead of seek(5,2), do manual offset
f.seek(f.tell() - 5, 0)
print("After moving 5 back from end:", f.tell())

# same for relative seeks (must use binary mode, or do manual math)
f.seek(6, 0)
print("After seeking to 6 from beginning:", f.tell())

f.close()