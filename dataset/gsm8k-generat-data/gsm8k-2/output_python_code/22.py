def solution():
    """Samantha’s last name has three fewer letters than Bobbie’s last name. If Bobbie took two letters off her last name, she would have a last name twice the length of Jamie’s. Jamie’s full name is Jamie Grey. How many letters are in Samantha’s last name?"""
    jamie_last_name = "Grey"
    bobbie_last_name = jamie_last_name * 2
    bobbie_last_name = bobbie_last_name[:-2]
    samantha_last_name = bobbie_last_name[:-3]
    result = len(samantha_last_name)
    return result

print(solution())