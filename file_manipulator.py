import sys
import os

def reverse(input_path, output_path):
    with open(input_path, 'r') as f:
        content = f.read()
    with open(output_path, 'w') as f:
        f.write(content[::-1])

def copy_file(input_path, output_path):
    with open(input_path, 'r') as f:
        content = f.read()
    with open(output_path, 'w') as f:
        f.write(content)

def duplicate_contents(input_path, n):
    with open(input_path, 'r') as f:
        content = f.read()
    with open(input_path, 'w') as f:
        f.write(content * int(n))

def replace_string(input_path, needle, newstring):
    with open(input_path, 'r') as f:
        content = f.read()
    with open(input_path, 'w') as f:
        f.write(content.replace(needle, newstring))

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print("No command provided.")
        sys.exit(1)

    command = args[1]

    try:
        if command == "reverse":
            reverse(args[2], args[3])
        elif command == "copy":
            copy_file(args[2], args[3])
        elif command == "duplicate-contents":
            duplicate_contents(args[2], args[3])
        elif command == "replace-string":
            replace_string(args[2], args[3], args[4])
        else:
            print(f"Unknown command: {command}")
    except IndexError:
        print("Not enough arguments for the command.")
    except FileNotFoundError:
        print("File not found.")
