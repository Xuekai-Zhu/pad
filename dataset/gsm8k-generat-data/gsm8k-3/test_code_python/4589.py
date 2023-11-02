def solution():
    """Every Halloween one house in the neighborhood gives out toothbrushes instead of candy, so it always gets egged and covered in toilet paper. If the owner spends 15 seconds cleaning up each egg and 30 minutes cleaning up each roll of toilet paper, how long (in minutes) will they have to spend cleaning up 60 eggs and 7 rolls of toilet paper?"""
    # Define the time it takes to clean up one egg and one roll of toilet paper
    EGG_TIME = 15 / 60 # convert seconds to minutes
    TP_TIME = 30

    # Calculate the total time to clean up the eggs
    egg_time = 60 * EGG_TIME

    # Calculate the total time to clean up the toilet paper
    tp_time = 7 * TP_TIME

    # Calculate the total cleaning time
    total_time = egg_time + tp_time

    # Display the total cleaning time
    result = total_time
    return result

print(solution())