# string_utils.py

def reverse_string(s):
    """Return the reverse of the input string."""
    return s[::-1]

def capitalize_string(s):
    """Return the input string with the first letter capitalized."""
    if s:
        return s[0].upper() + s[1:].lower()
    return ""

def upper_case_string(s):
    """Return the input string in uppercase."""
    return s.upper()

def lower_case_string(s):
    """Return the input string in lowercase."""
    return s.lower()
