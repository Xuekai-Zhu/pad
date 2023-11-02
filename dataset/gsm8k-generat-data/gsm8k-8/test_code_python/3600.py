def solution():
    # Convert Jane's stick length from feet to inches
    sarah_stick_length = 2 * 12
    jane_stick_length = sarah_stick_length - 24

    # Calculate the length of the portion not covered in dirt on Pat's stick
    pat_clean_length = 30 - 7

    # Calculate the length of the portion not covered in dirt on Sarah's stick
    sarah_clean_length = pat_clean_length / 2

    result = jane_stick_length
    return result

print(solution())