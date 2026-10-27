# Course 07 – Python Lab Notebook Summary

> Note: The original notebook files in the Python task folder were left unchanged. This document is a concise combined summary of the relevant Python exercises and concepts.

## Overview

This section of the course focused on learning Python through practical cybersecurity examples. The exercises covered variable assignment, loops, functions, conditionals, file handling, regular expressions, and algorithm design.

The notebooks included:

- Assign Python variables
- Create loops
- Create more functions
- Define and call a function
- Develop an algorithm
- Import and parse a text file
- Use regular expressions to find patterns
- Create a conditional statement
- Practice writing Python code

---

## 1) Variables and Data Types

In the variables lab, the goal was to store security-related values such as:

- device IDs
- approved usernames
- login attempt counts
- login status

Example:

```python
device_id = "72e08x0"
username_list = ["madebowa", "jnguyen", "tbecker"]
```

Key learning points:

- strings are stored with quotes
- lists are stored in square brackets
- `type()` can be used to identify the data type of a variable

This is useful in cybersecurity because analysts often work with usernames, device IDs, IP addresses, and lists of approved access values.

---

## 2) Loops and Repetition

The loop exercises introduced `for` loops and `while` loops for repeating actions.

Example:

```python
for i in ip_addresses:
    print(i)
```

and:

```python
connection_attempts = 0
while connection_attempts < 3:
    print("Connection could not be established")
    connection_attempts = connection_attempts + 1
```

Use cases from the labs included:

- displaying multiple connection warnings
- checking each IP address against an allow list
- repeating a message until a condition is met

This is a common pattern in automation, especially when reviewing multiple login attempts or network events.

---

## 3) Functions

The function labs introduced both built-in and user-defined functions.

Example:

```python
def alert():
    print("Potential security issue. Investigate further.")

alert()
```

Other examples included:

```python
def analyze_logins(username, current_day_logins):
    print("Current day login total for", username, "is", current_day_logins)
```

Key concepts:

- `def` creates a function
- parameters allow values to be passed into a function
- functions reduce repeated code and make scripts easier to maintain

---

## 4) Conditionals and Decision-Making

The conditional statement labs focused on evaluating conditions before taking action.

Example:

```python
if system == "OS 2":
    print("no update needed")
elif system == "OS 1" or system == "OS 3":
    print("update needed")
```

This was applied to:

- checking whether an OS requires an update
- verifying whether a user is approved to access a device
- deciding whether an IP is allowed or not

The logic used in these labs reflects real security processes such as user authorization and system monitoring.

---

## 5) File Handling and Parsing

The file import lab showed how to read text files and work with their contents in Python.

Example:

```python
with open(import_file, "r") as file:
    text = file.read()

print(text)
```

Important ideas:

- `open()` reads or writes files
- `"r"` mode reads a file
- `"a"` mode appends new data to a file
- `.split()` can separate a large string into a list of lines or values

This is useful for analyzing security logs and appending missing entries while keeping the data structured.

---

## 6) Regular Expressions

The regular expression lab focused on using Python to identify patterns in text data.

Example device ID match:

```python
target_pattern = "r15\w+"
re.findall(target_pattern, devices)
```

Example IP pattern:

```python
pattern = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
valid_ip_addresses = re.findall(pattern, log_file)
```

This was used to:

- find devices requiring updates
- filter valid IP addresses from a noisy log
- compare extracted IPs with a list of flagged addresses

This is a strong example of how Python supports automation and analysis in cybersecurity.

---

## 7) Algorithm Design

The algorithm lab used Python to simulate a real access control workflow:

- approved users and approved devices are stored in synchronized lists
- new users can be appended to the lists
- removed users can be deleted from the lists
- a username can be checked against the approved list

Example:

```python
if username in approved_users:
    print("The username", username, "is approved to access the system.")
else:
    print("The username", username, "is not approved to access the system.")
```

This demonstrates how Python can be used to automate validation tasks that support access control and system security.

---

## 8) Core Skills Developed

Across all of the notebook exercises, the following skills were practiced:

- writing Python comments and basic scripts
- assigning and printing variables
- using strings, lists, and numbers correctly
- writing `for` and `while` loops
- defining reusable functions
- applying conditional logic
- reading and writing files
- using regular expressions for pattern matching
- designing simple algorithms for security tasks

---

## 9) Summary

The Python tasks in Course 07 show how programming can be applied directly to cybersecurity work. The notebooks taught foundational Python skills in a security context, including access checks, log parsing, IP validation, update detection, and repeated task automation.

These concepts form the foundation for using Python to support monitoring, analysis, and operational workflows in real-world security environments.
