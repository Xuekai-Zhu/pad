def solution():
    """Pat’s computer password is made up of several kinds of alphanumeric and symbol characters for security. He uses a string of eight random lowercase letters, a string half that length of alternating upper case letters and numbers, and one symbol on each end of the password. How many characters in all is Pat‘s computer password?"""
    lowercase_length = 8
    uppercase_number_length = lowercase_length // 2
    symbol_length = 2
    uppercases_and_numbers = ""
    for i in range(uppercase_number_length):
        if i % 2 == 0:
            uppercases_and_numbers += "A"
        else:
            uppercases_and_numbers += "1"
            
    password_length = lowercase_length + len(uppercases_and_numbers) + symbol_length
    result = password_length
    return result

print(solution())