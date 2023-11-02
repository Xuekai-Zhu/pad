def solution():
    required_length = 15
    has_uppercase = False # the standard alphabet doesn't have uppercase letters
    has_lowercase = False # the standard alphabet doesn't have lowercase letters
    has_numbers = False # binary numbers only have 0 and 1
    has_symbols = False # the standard alphabet doesn't have symbols
    if len(binary_numbers + standard_alphabet) >= required_length:
        for char in binary_numbers + standard_alphabet:
            if char.isupper():
                has_uppercase = True
            elif char.islower():
                has_lowercase = True
            elif char.isdigit():
                has_numbers = True
            else:
                has_symbols = True
        if has_uppercase and has_lowercase and has_numbers and has_symbols:
            result = "yes"
        else:
            result = "no"
    else:
        result = "no"
    return result

print(solution())