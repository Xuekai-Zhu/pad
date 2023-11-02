def solution():
    """Pat’s computer password is made up of several kinds of alphanumeric and symbol characters for security. He uses a string of eight random lowercase letters, a string half that length of alternating upper case letters and numbers, and one symbol on each end of the password. How many characters in all is Pat‘s computer password?"""
    lowercase_letters = 8
    alternating_characters = lowercase_letters // 2
    symbol_count = 2
    total_characters = lowercase_letters + alternating_characters + symbol_count
    result = total_characters
    return result

print(solution())