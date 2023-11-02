def solution():
    # Jamie's full name contains 9 letters
    jamie_name = "Jamie Grey"
    jamie_len = len(jamie_name) - 1  # exclude the space between first and last name

    # Bobbie's last name is 2 letters longer than Jamie's last name
    bobbie_last_len = jamie_len + 2

    # Bobbie's last name would be twice as long if she had 2 letters added
    bobbie_new_last_len = bobbie_last_len + 2
    bobbie_new_first_len = len("Bobbie")  # assume Bobbie's first name is 6 letters
    bobbie_new_len = bobbie_new_first_len + bobbie_new_last_len

    # Samantha's last name is 3 letters shorter than Bobbie's last name
    samantha_last_len = bobbie_last_len - 3

    result = samantha_last_len
    return result

print(solution())