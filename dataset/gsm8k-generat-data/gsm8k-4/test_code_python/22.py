def solution():
    """Samantha’s last name has three fewer letters than Bobbie’s last name. If Bobbie took two letters off her last name, she would have a last name twice the length of Jamie’s. Jamie’s full name is Jamie Grey. How many letters are in Samantha’s last name?"""
    # Define Jamie's last name
    jamie_last_name = "Grey"

    # Calculate the length of Jamie's last name
    jamie_last_name_length = len(jamie_last_name)

    # Calculate the length of Bobbie's last name
    bobbie_last_name_length = 2 * jamie_last_name_length + 2

    # Calculate the length of Samantha's last name
    samantha_last_name_length = bobbie_last_name_length - 3

    # Return the result
    result = samantha_last_name_length
    return result

print(solution())