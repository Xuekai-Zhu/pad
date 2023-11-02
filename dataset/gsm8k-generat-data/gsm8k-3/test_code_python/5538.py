def solution():
    """The ratio of cows to bulls in a barn is 10:27. If there are 555 cattle on the farm, how many bulls are on the farm?"""
    # Define the ratio of cows to bulls
    COWS_TO_BULLS_RATIO = 10 / 27

    # Get the total number of cattle on the farm
    total_cattle = 555

    # Calculate the number of cows and bulls using the ratio
    cattle_sum = 10 + 27
    cow_fraction = 10 / cattle_sum
    bull_fraction = 27 / cattle_sum
    cows = total_cattle * cow_fraction
    bulls = total_cattle * bull_fraction

    # Display the number of bulls on the farm
    result = bulls
    return result

print(solution())