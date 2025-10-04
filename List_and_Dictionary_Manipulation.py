# n = int(input("number of entries: "))
# people = [{"name": input("name: "), "age": int(input("age: ")), "city": input("city: ")} for i in range(n)]
people = [
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'age': 22, 'city': 'San Francisco'},
    {'name': 'Charlie', 'age': 35, 'city': 'Los Angeles'}
]
age = []
print("```")
print("Names of people older than 25:")
for item in people:
    age.append(item.get("age"))
    if item.get("age") > 25:
        print(item.get("name"))
print("""
      """)
print("Sorted by age (descending):")
for i in reversed(sorted(age)):
    for item in people:
        if item.get("age") == i:
            print(item)
            people.remove(item)
print("""
      """)
print("```")