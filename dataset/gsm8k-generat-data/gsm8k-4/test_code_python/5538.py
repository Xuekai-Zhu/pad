def solution():
    """The ratio of cows to bulls in a barn is 10:27. If there are 555 cattle on the farm, how many bulls are on the farm?"""
    # Define the ratio of cows to bulls
    ratio_cows_to_bulls = 10/27

    # Calculate the total number of cattle on the farm
    total_cattle = 555

    # Calculate the number of cows on the farm
    num_cows = total_cattle / (1 + ratio_cows_to_bulls)

    # Calculate the number of bulls on the farm
    num_bulls = total_cattle - num_cows

    result = num_bulls
    return result

print(solution())