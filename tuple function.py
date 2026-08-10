
a = (10, 20, 30, 20, 40)

print("Original Tuple:", a)

#  count
print("Count of 20:", a.count(20))

#  index
print("Index of 30:", a.index(30))

#  len
print("Length:", len(a))

# max
print("Maximum:", max(a))

# min
print("Minimum:", min(a))

#  sum
print("Sum:", sum(a))

#  Access tuple item
print("First item:", a[0])
print("Last item:", a[-1])

# Slicing
print("First 3 items:", a[0:3])

#  Tuple length using loop
count = 0
for item in a:
    count = count + 1

print("Length using loop:", count)

#  Print all items
print("Tuple items:")

for item in a:
    print(item)
