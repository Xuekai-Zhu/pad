def solution():
    """Pat's stick is 30 inches long. He covers 7 inches of the stick in dirt. The portion that is not covered in dirt is half as long as Sarah’s stick. Jane’s stick is two feet shorter than Sarah’s stick. How many inches long is Jane’s stick?"""
    # Define the length of Pat's stick and the portion covered in dirt
    pat_stick_length = 30
    pat_dirt_length = 7

    # Calculate the length of the portion of Pat's stick not covered in dirt
    pat_clean_length = pat_stick_length - pat_dirt_length

    # Calculate the length of Sarah's stick
    sarah_stick_length = pat_clean_length * 2

    # Calculate the length of Jane's stick, which is two feet (24 inches) shorter than Sarah's stick
    jane_stick_length = sarah_stick_length - 24

    # Display the length of Jane's stick in inches
    result = jane_stick_length
    return result

print(solution())