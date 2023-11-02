def solution():
    jamie_last_name = "Grey"
    bobbie_last_name = jamie_last_name * 2  # Bobbie's last name is twice as long as Jamie's
    bobbie_last_name = bobbie_last_name[:len(bobbie_last_name)-2]  # Bobbie takes off two letters
    samantha_last_name = bobbie_last_name[:len(bobbie_last_name)-3]  # Samantha's last name has three fewer letters than Bobbie's last name
    result = len(samantha_last_name)
    return result

print(solution())