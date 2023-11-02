def solution():
    """While at the lake, Cohen saw 300 fish-eater birds that had migrated into the area recently walking by the lake, eating the fish they had caught. The number of birds at the lake doubled on the second day and reduced by 200 on the third day. How many fish-eater birds did Cohen see in the three days?"""
    # Define the number of birds Cohen saw on the first day
    birds_day1 = 300

    # Calculate the number of birds on the second day
    birds_day2 = birds_day1 * 2

    # Calculate the number of birds on the third day
    birds_day3 = birds_day2 - 200

    # Calculate the total number of birds seen in the three days
    total_birds = birds_day1 + birds_day2 + birds_day3

    # return the result
    result = total_birds
    return result

print(solution())