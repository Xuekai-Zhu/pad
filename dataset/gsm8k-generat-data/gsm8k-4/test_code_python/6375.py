def solution():
    """Pat’s computer password is made up of several kinds of alphanumeric and symbol characters for security.
    He uses a string of eight random lowercase letters, a string half that length of alternating upper case
    letters and numbers, and one symbol on each end of the password. How many characters in all is Pat‘s computer password?"""
    # Define the number of lowercase letters and the number of alternating uppercase letters and numbers
    lowercase_count = 8
    alternating_count = lowercase_count // 2

    # Define the number of symbols at the ends of the password
    symbol_count = 2

    # Calculate the total number of characters in the password
    total_count = lowercase_count + alternating_count + symbol_count * 2

    # return the result
    result = total_count
    return result

print(solution())