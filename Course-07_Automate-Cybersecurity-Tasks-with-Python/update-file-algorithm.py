# Update File Algorithm
# Google Cybersecurity Certificate – Course 7
#
# This script reads an allow list of approved IP addresses from a file,
# removes any IP addresses that appear on a remove list (revoked access),
# and writes the updated allow list back to the file.


def update_file(import_file, remove_list):
    """
    Reads an allow list file, removes IPs in remove_list, and saves the result.

    Parameters:
        import_file (str): Path to the allow list text file.
        remove_list (list): List of IP addresses to remove from the allow list.
    """

    # --- Step 1: Open and read the allow list file ---
    with open(import_file, "r") as file:
        ip_addresses = file.read()

    # --- Step 2: Convert the string into a list ---
    ip_addresses = ip_addresses.split()

    # --- Step 3: Remove IPs that are in the remove_list ---
    for element in remove_list:
        if element in ip_addresses:
            ip_addresses.remove(element)

    # --- Step 4: Convert the list back into a string ---
    ip_addresses = "\n".join(ip_addresses)

    # --- Step 5: Write the updated list back to the file ---
    with open(import_file, "w") as file:
        file.write(ip_addresses)

    print(f"Updated allow list saved to '{import_file}'.")
    print("Current allow list:")
    print(ip_addresses)


# -------------------------------------------------------------------
# Example usage
# -------------------------------------------------------------------

# The file containing the current allow list (one IP per line)
import_file = "allow_list.txt"

# IP addresses whose access has been revoked
remove_list = [
    "192.168.97.105",
    "192.168.158.170",
    "192.168.201.40",
    "192.168.58.57"
]

update_file(import_file, remove_list)
