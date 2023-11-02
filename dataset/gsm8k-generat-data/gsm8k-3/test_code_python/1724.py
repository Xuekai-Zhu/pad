def solution():
    """There were 18 stamps in Parker’s scrapbook. If Addie put one fourth of her 72 stamps in Parker’s scrapbook, how many stamps does he have now?"""
    # Define the initial number of stamps in Parker's scrapbook and the number of stamps added by Addie
    parker_stamps = 18
    addie_stamps = 72/4

    # Calculate the new total number of stamps
    total_stamps = parker_stamps + addie_stamps

    # Display the new total number of stamps
    result = total_stamps
    return result

print(solution())