# file_operations.py

def read_file(file_path):
    """Read the contents of a file and return it as a string.
    
    Args:
        file_path (str): Path to the file to read.
    
    Returns:
        str: Contents of the file.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."
    except IOError as e:
        return f"An error occurred: {e}"

def write_file(file_path, data):
    """Write data to a file, overwriting the file if it exists.
    
    Args:
        file_path (str): Path to the file to write to.
        data (str): Data to write to the file.
    
    Returns:
        str: Success message or error message.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(data)
        return "Data written to file successfully."
    except IOError as e:
        return f"An error occurred: {e}"

def append_to_file(file_path, data):
    """Append data to a file.
    
    Args:
        file_path (str): Path to the file to append to.
        data (str): Data to append to the file.
    
    Returns:
        str: Success message or error message.
    """
    try:
        with open(file_path, 'a') as file:
            file.write(data)
        return "Data appended to file successfully."
    except IOError as e:
        return f"An error occurred: {e}"
