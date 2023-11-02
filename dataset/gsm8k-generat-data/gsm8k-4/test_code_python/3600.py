def solution():
    """Pat's stick is 30 inches long. He covers 7 inches of the stick in dirt. The portion that is not covered in dirt is half as long as Sarah’s stick. Jane’s stick is two feet shorter than Sarah’s stick. How many inches long is Jane’s stick?"""
    # Define the length of Pat's stick and the portion covered in dirt
    pat_stick = 30
    pat_dirt = 7

    # Calculate the length of the portion not covered in dirt
    pat_clean = pat_stick - pat_dirt

    # Calculate the length of Sarah's stick
    sarah_stick = pat_clean * 2

    # Calculate the length of Jane's stick
    jane_stick = sarah_stick - 24

    result = jane_stick
    return result

print(solution())