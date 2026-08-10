student = {
    "name": "Amaan",
    "age": 20,
    "course": "BSc IT"
}

#  Print Dictionary
print(student)

#  Access value
print(student["name"])

#  Get value
print(student.get("age"))

#  Get all keys
print(student.keys())

#  Get all values
print(student.values())

#  Get key and value
print(student.items())

#  Add new item
student["city"] = "Ahmedabad"
print(student)

#  Change value
student["age"] = 21
print(student)

#  Remove item
student.pop("age")
print(student)

#  Check key
if "name" in student:
    print("Found")
else:
    print("Not Found")

#  Length
print(len(student))

#  Copy Dictionary
new_student = student.copy()
print(new_student)

#  Print keys using loop
for x in student:
    print(x)

#  Print values using loop
for x in student.values():
    print(x)

#  Clear Dictionary
student.clear()
print(student)
