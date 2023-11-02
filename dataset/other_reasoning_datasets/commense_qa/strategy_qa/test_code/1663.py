def solution():
    zip_code_length = 9
    digits_memorized = 5
    if digits_memorized / zip_code_length > 0.5:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())