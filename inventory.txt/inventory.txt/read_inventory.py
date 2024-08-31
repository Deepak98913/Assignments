def read_and_display_file(file_path):
    """Open a file and display its contents line by line.

    Args:
        file_path (str): Path to the file to read.
    """
    try:
        with open(file_path, 'r') as file:
            # Read and print each line in the file
            for line in file:
                print(line, end='')  # `end=''` to avoid adding extra newlines
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")

# File path
file_path = 'inventory.txt'

# Read and display the file contents
read_and_display_file(file_path)
