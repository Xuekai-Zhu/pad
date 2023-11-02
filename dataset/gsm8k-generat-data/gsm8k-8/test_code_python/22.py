def solution():
    # Define Jamie's last name
    jamie_last_name = "Grey"
    jamie_last_name_length = len(jamie_last_name)

    # Calculate Bobbie's last name length
    bobbie_last_name_length = jamie_last_name_length * 2

    # Calculate Bobbie's current last name length
    bobbie_current_last_name_length = bobbie_last_name_length + 2

    # Calculate Samantha's last name length
    samantha_last_name_length = bobbie_current_last_name_length - 3

    result = samantha_last_name_length
    return result

print(solution())