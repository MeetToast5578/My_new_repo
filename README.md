# python-data-types---task-2

```markdown
# Python Tasks: Data Types, Loops, and Conditional Statements (Medium Difficulty)

## Task 1: Advanced Data Types - List and Dictionary Manipulation
**Problem**: Write a Python program that takes a list of dictionaries where each dictionary contains information about a person (`name`, `age`, and `city`). The program should:

1. Print the names of all people who are older than 25.
2. Sort the list by `age` in descending order and print the sorted list.

**Example Input**:
```python
people = [
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'age': 22, 'city': 'San Francisco'},
    {'name': 'Charlie', 'age': 35, 'city': 'Los Angeles'}
]
```

**Example Output**:
```
Names of people older than 25:
Alice
Charlie

Sorted by age (descending):
[{'name': 'Charlie', 'age': 35, 'city': 'Los Angeles'},
 {'name': 'Alice', 'age': 30, 'city': 'New York'},
 {'name': 'Bob', 'age': 22, 'city': 'San Francisco'}]
```

---

## Task 2: Loops - Find Prime Numbers in a Range
**Problem**: Write a Python program that takes a range of numbers (start, end) and prints all prime numbers in that range.

**Example Input**:
```
start = 10
end = 50
```

**Example Output**:
```
Prime numbers between 10 and 50:
11
13
17
19
23
29
31
37
41
43
47
```

---

## Task 6: Dictionary - Frequency Counter
**Problem**: Write a Python program that counts the frequency of each word in a given string. The program should ignore case and punctuation.

**Example Input**:
```
text = "Hello world! Hello everyone. Welcome to the world of Python."
```

**Example Output**:
```
{'hello': 2, 'world': 2, 'everyone': 1, 'welcome': 1, 'to': 1, 'the': 1, 'of': 1, 'python': 1}
```

---

## Task 13: List Comprehension - Square Numbers
**Problem**: Write a Python program that takes a list of integers and generates a new list with the square of each number using list comprehension.

**Example Input**:
```
numbers = [1, 2, 3, 4, 5]
```

**Example Output**:
```
[1, 4, 9, 16, 25]
```

---

## Task 15: Sorting - Sort Words by Length
**Problem**: Write a Python program that sorts a list of words by their length (from shortest to longest).

**Example Input**:
```python
words = ["apple", "banana", "pear", "grape"]
```

**Example Output**:
```
['pear', 'grape', 'apple', 'banana']
```

---