import string
import os
import itertools
from tqdm import tqdm

def generate_strings(min_length, max_length):
    characters = string.printable
    for length in range(min_length, max_length + 1):
        yield from (''.join(p) for p in itertools.product(characters, repeat=length))

def write_to_file(strings, filename):
    print(f"Attempting to write passwords to: {filename}")
    while True:
        try:
            with open(filename, 'w') as f:
                for string in tqdm(strings, desc="Generating strings"):
                    f.write(string + '\n')
            break
        except IOError as e:
            print(f"An error occurred while accessing {filename}: {e}\n")
            filename = input("Choose destination path (default: 'strings.txt' in the current directory): ") or filename

def get_integer_input(prompt, default):
    while True:
        try:
            value = input(prompt) or default
            return int(value)
        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")

def main():
    print(f"CSWC's Brute Typewriter\n")
    filename = os.path.join(os.getcwd(), 'strings.txt')
    try:
        min_length = get_integer_input("Minimum string length (default: 1): ", 1)
        max_length = get_integer_input("Maximum string length (default: 2): ", 2)
        filename = input("Choose destination path (default: 'strings.txt' in the current directory): ") or filename
        strings = generate_strings(min_length, max_length)
        write_to_file(strings, filename)
    except KeyboardInterrupt:
        print(f"\nProcess interrupted; writing generated strings to {filename}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()