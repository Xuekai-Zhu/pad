def solution():
    lowercase_letters = 8  # Pat uses a string of eight random lowercase letters
    alternating_chars = 4  # Pat uses a string half the length of alternating upper case letters and numbers
    symbol_chars = 2  # Pat adds one symbol on each end of the password

    # Calculate the total number of characters in Pat's password
    total_chars = lowercase_letters + alternating_chars + symbol_chars * 2
    result = total_chars
    return result

print(solution())