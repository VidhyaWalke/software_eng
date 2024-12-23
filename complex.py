import os

def factorial(n):
    """Recursive function to calculate factorial."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def save_to_file(filename, data):
    """Saves a list of data to a file."""
    with open(filename, 'w') as f:
        for item in data:
            f.write(f"{item}\n")

def read_and_square(filename):
    """Reads numbers from a file, squares them, and returns the result."""
    squared_numbers = []
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            for line in f:
                try:
                    num = int(line.strip())
                    squared_numbers.append(num ** 2)
                except ValueError:
                    pass  # Ignore lines that are not integers
    return squared_numbers

def main():
    print("Factorial Calculator and File Processor")
    
    # Get a number from the user for factorial calculation
    num = int(input("Enter a number to calculate its factorial: "))
    print(f"The factorial of {num} is {factorial(num)}")
    
    # Generate numbers from 1 to num and save to a file
    filename = "numbers.txt"
    numbers = list(range(1, num + 1))
    save_to_file(filename, numbers)
    print(f"Numbers 1 to {num} saved to {filename}")
    
    # Read numbers from the file, square them, and display
    squared = read_and_square(filename)
    print(f"Squared numbers read from {filename}: {squared}")

if __name__ == "__main__":
    main()
