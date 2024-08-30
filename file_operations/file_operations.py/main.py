# main.py

from file_operations import read_file, write_file, append_to_file

def test_file_operations():
    file_path = 'example.txt'

    # Write to file
    write_message = write_file(file_path, "Hello, world!\n")
    print(write_message)

    # Append to file
    append_message = append_to_file(file_path, "Appending some more text.\n")
    print(append_message)

    # Read from file
    content = read_file(file_path)
    print("File content:")
    print(content)

# Call the test function
test_file_operations()
