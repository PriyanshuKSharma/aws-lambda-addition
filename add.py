def add_numbers_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    # Assuming the file contains two lines, each representing a number
    num1 = float(lines[0].strip())
    num2 = float(lines[1].strip())
    result = num1 + num2
    print("The sum is:", result)

if __name__ == "__main__":
    filename = "input.txt"  # Specify the filename here
    add_numbers_from_file(filename)
