def solution():
    """Pat’s computer password is made up of several kinds of alphanumeric and symbol characters for security. He uses a string of eight random lowercase letters, a string half that length of alternating upper case letters and numbers, and one symbol on each end of the password. How many characters in all is Pat‘s computer password?"""
    # Define the length of each part of the password
    lowercase_len = 8
    alternating_len = lowercase_len // 2
    symbol_len = 2

    # Calculate the length of the password
    password_len = lowercase_len + alternating_len + symbol_len * 2

    # Display the length of the password
    result = password_len
    return result

print(solution())