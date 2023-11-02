def solution():
    """Samantha's last name has three fewer letters than Bobbie's last name. If Bobbie took two letters off her last name, she would have a last name twice the length of Jamie's. Jamie's full name is Jamie Grey. How many letters are in Samantha's last name?"""
    jamie_name_length = len("Grey")
    bobbie_name_length = 2 * jamie_name_length + 2
    samantha_name_length = bobbie_name_length - 3
    result = samantha_name_length
    return result

print(solution())