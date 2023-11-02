def solution():
    """Samantha’s last name has three fewer letters than Bobbie’s last name. If Bobbie took two letters off her last name, she would have a last name twice the length of Jamie’s. Jamie’s full name is Jamie Grey. How many letters are in Samantha’s last name?"""
    # Define Jamie's last name length
    jamie_last_name = len("Grey")

    # Define Bobbie's potential last name length after removing 2 letters
    bobbie_last_name = jamie_last_name * 2

    # Define Bobbie's current last name length
    bobbie_current_last_name = bobbie_last_name + 2

    # Define Samantha's last name length, which is 3 less than Bobbie's current last name length
    samantha_last_name = bobbie_current_last_name - 3

    # Return the result
    result = samantha_last_name
    return result

print(solution())