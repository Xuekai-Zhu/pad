def solution():
    """Mary and Ann are going sledding. Mary slides down a hill that's 630 feet long at a speed of 90 feet/minute. Ann slides down a hill that's 800 feet long at a rate of 40 feet/minute. How much longer does Ann's trip take than Mary?"""
    # Calculate the time it takes for Mary to slide down the hill
    distance_mary = 630
    speed_mary = 90
    time_mary = distance_mary / speed_mary

    # Calculate the time it takes for Ann to slide down the hill
    distance_ann = 800
    speed_ann = 40
    time_ann = distance_ann / speed_ann

    # Calculate the difference in time between Mary and Ann
    time_difference = time_ann - time_mary

    # Display the time difference
    result = time_difference
    return result

print(solution())