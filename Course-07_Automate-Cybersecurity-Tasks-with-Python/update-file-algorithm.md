# Algorithm for File Updates in Python

**Author:** [Your Name]  
**Date:** [Date]  
**Language:** Python 3  
**Course:** Google Cybersecurity Certificate – Course 7: Automate Cybersecurity Tasks with Python

---

## Project Description

At my organization, access to restricted content is controlled using an allow list of approved IP addresses stored in a file called `allow_list.txt`. A separate remove list identifies IP addresses that should no longer have access. I developed a Python algorithm to automate the process of removing revoked IP addresses from the allow list and updating the file.

---

## Open the File That Contains the Allow List

I used a `with` statement and the `open()` function in `"r"` (read) mode to open `allow_list.txt` and read its contents:

```python
with open(import_file, "r") as file:
    ip_addresses = file.read()
```

The `with` keyword ensures the file is properly closed after use. The `.read()` method returns the file contents as a single string assigned to `ip_addresses`.

---

## Convert the String into a List

Because I need to iterate over individual IP addresses and remove specific ones, I converted the string into a list using the `.split()` method:

```python
ip_addresses = ip_addresses.split()
```

`.split()` splits on whitespace by default, converting each line (each IP address) into a separate list element.

---

## Iterate Through the Remove List

I used a `for` loop to iterate through each IP address in `remove_list`. For each element, I checked whether it existed in `ip_addresses` and removed it if so:

```python
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)
```

The `if` conditional prevents an error in cases where an IP on the remove list is not present in the allow list (e.g., it was already removed).

---

## Update the File with the Revised List

After removing the revoked IP addresses, I converted the updated list back into a string using `.join()`, with each IP on a new line:

```python
ip_addresses = "\n".join(ip_addresses)
```

I then opened the file in `"w"` (write) mode and wrote the updated content back, overwriting the old allow list:

```python
with open(import_file, "w") as file:
    file.write(ip_addresses)
```

---

## Summary

| Step | Action | Python Used |
|------|--------|-------------|
| 1 | Open and read the allow list file | `open()`, `.read()`, `with` |
| 2 | Convert string to list | `.split()` |
| 3 | Remove revoked IPs | `for` loop, `if`, `.remove()` |
| 4 | Convert list back to string | `"\n".join()` |
| 5 | Write updated list to file | `open()` in `"w"` mode, `.write()` |

This algorithm automates a manual process, reducing the risk of human error and saving the security team time. It can be scheduled to run regularly or triggered as part of an access review workflow.
