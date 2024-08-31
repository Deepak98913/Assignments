def calculate_total_expenses(file_path):
    """Read a file containing expenses and calculate the total amount spent.

    Args:
        file_path (str): Path to the file containing expense data.
    
    Returns:
        float: Total amount spent on expenses.
    """
    total_amount = 0.0
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Assuming each line contains an expense amount, e.g., "50.75"
                try:
                    amount = float(line.strip())  # Convert line to float after stripping whitespace
                    total_amount += amount
                except ValueError:
                    print(f"Warning: Could not convert '{line.strip()}' to a number.")
    
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")
    
    return total_amount

# File path
file_path = 'expenses.txt'

# Calculate and display total expenses
total_expenses = calculate_total_expenses(file_path)
print(f"Total amount spent: ${total_expenses:.2f}")

