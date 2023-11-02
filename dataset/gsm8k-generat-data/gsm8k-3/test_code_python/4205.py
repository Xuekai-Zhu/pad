def solution():
    """While at the lake, Cohen saw 300 fish-eater birds that had migrated into the area recently walking by the lake, eating the fish they had caught. The number of birds at the lake doubled on the second day and reduced by 200 on the third day. How many fish-eater birds did Cohen see in the three days?"""
    # Define the number of fish-eater birds on the first day
    day_1_birds = 300

    # Calculate the number of fish-eater birds on the second day
    day_2_birds = day_1_birds * 2

    # Calculate the number of fish-eater birds on the third day
    day_3_birds = day_2_birds - 200

    # Calculate the total number of fish-eater birds seen in three days
    total_birds = day_1_birds + day_2_birds + day_3_birds

    # Display the total number of fish-eater birds seen in three days
    result = total_birds
    return result

print(solution())