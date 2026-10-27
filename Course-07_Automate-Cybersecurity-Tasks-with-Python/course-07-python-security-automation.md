# Course 07 – Automate Cybersecurity Tasks with Python

> Note: The original Python script and notebook materials were left unchanged. This file is a concise markdown summary of the relevant content and tasks.

## Overview

This course introduced Python as a practical tool for cybersecurity work. The main focus was automating routine security processes, analyzing logs, and using Python to identify suspicious activity more quickly and consistently than manual review.

The work covered in this course included:

- reading and updating files with allow lists and remove lists
- using loops and conditionals to make decisions in scripts
- parsing text data from logs and configuration files
- using regular expressions to locate device IDs and IP addresses
- identifying suspicious or flagged values for investigation

---

## 1) File Update Algorithm

### Scenario

A security team maintains an allow list of approved IP addresses in a file. A second list identifies IP addresses that must no longer have access. The goal is to remove revoked addresses from the allow list automatically.

### Python approach

A typical solution uses a `with` statement to read the file, then converts the content into a list, removes unauthorized entries, and writes the updated list back.

```python
with open(import_file, "r") as file:
    ip_addresses = file.read()

ip_addresses = ip_addresses.split()

for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

ip_addresses = "\n".join(ip_addresses)

with open(import_file, "w") as file:
    file.write(ip_addresses)
```

### Why it matters

This type of Python script is useful because it:

- removes the need for manual edits to security files
- reduces the chance of human error
- allows the team to manage access lists efficiently and consistently
- supports repeatable operational tasks in a security environment

---

## 2) Regular Expressions for Pattern Matching

### Scenario

A security analyst is reviewing log data that includes device IDs and IP addresses. The analyst needs to filter information that matters for investigation and update tracking.

### Device ID extraction

A device ID starting with `r15` indicates a system that requires an update. The key pattern is:

```python
target_pattern = "r15\w+"
```

This matches strings that start with `r15` and continue with one or more alphanumeric characters.

Example extracted values:

```python
re.findall(target_pattern, devices)
```

Example output may include:

- `r151dm4`
- `r15xk9h`
- `r15u9q5`
- `r159r1u`

### IP address extraction

For a log file containing invalid and valid IP addresses, a regular expression can be used to match format-specific values.

A basic valid-IP pattern is:

```python
pattern = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
```

This pattern allows each octet to contain between one and three digits, which matches valid IPv4-like values.

```python
valid_ip_addresses = re.findall(pattern, log_file)
print(valid_ip_addresses)
```

This is useful because it allows analysts to:

- isolate relevant IP addresses from messy logs
- ignore malformed entries that do not follow expected IPv4 formatting
- compare extracted IPs with a list of flagged addresses

---

## 3) Flagging Suspicious IP Addresses

### Scenario

After extracting valid IP addresses, the next step is to compare them against a list of addresses previously identified as suspicious.

```python
flagged_addresses = ["192.168.190.178", "192.168.96.200", "192.168.174.117", "192.168.168.144"]
```

Then a loop can check whether each extracted address is flagged:

```python
for address in valid_ip_addresses:
    if address in flagged_addresses:
        print("The IP address", address, "has been flagged for further analysis.")
    else:
        print("The IP address", address, "does not require further analysis.")
```

This demonstrates how Python can help automate triage and investigation workflows.

---

## Key Python Concepts Used

The course introduced the following tools and concepts:

- `import re` for regular expressions
- `re.findall()` to return all matching values in a string
- `for` loops to iterate through lists
- `if` statements for conditional checks
- `open()` and file write modes for file management
- `.split()` and `"\n".join()` for working with list-based data

---

## Key Takeaways

- Python is a practical tool for automating security operations.
- Regular expressions help analysts extract meaningful information from logs and strings.
- Lists, conditionals, and loops make it easier to process and analyze large numbers of values.
- Automating repetitive tasks improves both speed and accuracy in cybersecurity work.

---

## Summary

The Python work in Course 07 focused on using code to solve real security problems efficiently. From filtering IP addresses to managing access lists, Python helps analysts automate tasks that would otherwise be repetitive, error-prone, or time-consuming.
