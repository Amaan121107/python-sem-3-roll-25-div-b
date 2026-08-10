a = [10, 20, 30, 20, 40]

print("Original List:", a)

#  append
a.append(50)
print("After append:", a)

#  insert
a.insert(1, 15)
print("After insert:", a)

#  remove
a.remove(20)
print("After remove:", a)

# pop
a.pop(2)
print("After pop:", a)

#  index
print("Index of 30:", a.index(30))

#  count
print("Count of 20:", a.count(20))

#  sort
a.sort()
print("After sort:", a)

#  reverse
print("After reverse:", a)

#  copy
b = a.copy()
print("Copied List:", b)

#  len
print("Length:", len(a))

# max
print("Maximum:", max(a))

#  min
print("Minimum:", min(a))

#  sum
print("Sum:", sum(a))


