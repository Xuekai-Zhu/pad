def solution():
    olivia_name_length = 16
    catherine_name_length = 18
    joseph_name_length = 18
    longest_name_length = max(olivia_name_length, catherine_name_length, joseph_name_length)
    if longest_name_length == olivia_name_length:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())