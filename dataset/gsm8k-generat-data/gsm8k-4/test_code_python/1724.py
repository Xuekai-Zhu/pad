def solution():
    """There were 18 stamps in Parker’s scrapbook. If Addie put one fourth of her 72 stamps in Parker’s scrapbook, how many stamps does he have now?"""
    # Define the initial number of stamps
    initial_stamps = 18

    # Calculate the number of stamps Addie put in
    addie_stamps = 72 // 4

    # Calculate the total number of stamps after Addie puts in her stamps
    total_stamps = initial_stamps + addie_stamps

    result = total_stamps
    return result

print(solution())