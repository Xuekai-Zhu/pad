def solution():
    """Bridget counted 14 shooting stars in the night sky. Reginald counted two fewer shooting stars than did Bridget, but Sam counted four more shooting stars than did Reginald. How many more shooting stars did Sam count in the night sky than was the average number of shooting stars observed for the three of them?"""
    # Define the number of shooting stars counted by Bridget
    bridget_count = 14

    # Define the number of shooting stars counted by Reginald
    reginald_count = bridget_count - 2

    # Define the number of shooting stars counted by Sam
    sam_count = reginald_count + 4

    # Calculate the average number of shooting stars observed
    average_count = (bridget_count + reginald_count + sam_count) / 3

    # Calculate how much more shooting stars Sam counted above the average
    more_count = sam_count - average_count

    result = more_count
    return result

print(solution())