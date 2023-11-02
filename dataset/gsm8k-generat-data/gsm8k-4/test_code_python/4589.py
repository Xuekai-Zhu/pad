def solution():
    """Every Halloween one house in the neighborhood gives out toothbrushes instead of candy, so it always gets egged and covered in toilet paper. If the owner spends 15 seconds cleaning up each egg and 30 minutes cleaning up each roll of toilet paper, how long (in minutes) will they have to spend cleaning up 60 eggs and 7 rolls of toilet paper?"""
    # Define the time it takes to clean up one egg and one roll of toilet paper
    EGG_CLEANUP_TIME = 15 # seconds
    TP_CLEANUP_TIME = 30 # minutes

    # Define the number of eggs and rolls of toilet paper to clean up
    eggs_to_clean = 60
    tp_to_clean = 7

    # Calculate the total time to clean up the eggs and toilet paper
    total_time = (eggs_to_clean * EGG_CLEANUP_TIME + tp_to_clean * TP_CLEANUP_TIME) / 60

    # Return the result
    result = total_time
    return result

print(solution())