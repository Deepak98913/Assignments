# main.py

from string_utils import reverse_string, capitalize_string, upper_case_string, lower_case_string

def test_string_utils():
    text = "hello World"

    print(f"Original Text: {text}")
    print(f"Reversed Text: {reverse_string(text)}")
    print(f"Capitalized Text: {capitalize_string(text)}")
    print(f"Uppercase Text: {upper_case_string(text)}")
    print(f"Lowercase Text: {lower_case_string(text)}")

# Call the test function
test_string_utils()
