def solution():
    # Define the length of the random lowercase letter string
    lowercase_length = 8

    # Define the length of the alternating upper case and number string
    alternating_length = int(lowercase_length / 2)

    # Define the number of symbols used (2)
    symbol_count = 2

    # Calculate the total length of the password
    password_length = lowercase_length + alternating_length + symbol_count

    # Return the result
    return password_length

print(solution())