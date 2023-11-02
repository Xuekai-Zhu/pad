def solution():
    # Calculate the number of characters in Pat's password
    num_lowercase = 8
    num_uppercase_numbers = 4
    num_symbols = 2
    total_chars = num_lowercase + num_uppercase_numbers + num_symbols*2
    result = total_chars
    return result

print(solution())