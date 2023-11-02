def solution():
    
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