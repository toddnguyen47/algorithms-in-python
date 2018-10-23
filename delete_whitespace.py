# Author: Todd Nguyen
# Last Updated: Oct 20, 2018 - 12:18

import re
import os.path

def replace_special_chars(str_input):
    special_chars = ["\\", "\"", ".", "(", ")"]
    for char in special_chars:
        str_input = str_input.replace(char, "".join(("\\", char)))

    return str_input


input_filename = input("Enter filename: ")

with open("index.html", "r") as file:
    data = file.read()

# Use positive look-ahead and positive look-behind to look for whitespace
pattern = "\s*(?=\<)|(?<=\>)\s*"
data = re.sub(pattern, "", data)
print(data)
print("")

produce_output = input("Would you like to export? (Y/N): ")

if produce_output.lower() == "y":
    output_filename = input("Enter output filename: ")
    if os.path.isfile(output_filename):
        # Make a copy
        with open(output_filename, "r") as file:
            backup = file.read()
        backup_filename = "".join((output_filename, ".bak"))
        with open(backup_filename, "w") as file:
            file.write(backup)

    with open(output_filename, "w") as file:
        file.write(data)
    
    print("Finished exporting.")

print("Thank you for using this program!")

