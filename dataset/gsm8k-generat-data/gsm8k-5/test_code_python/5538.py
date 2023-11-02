def solution():
    # Set up the ratio of cows to bulls
    ratio = 10/27

    # Calculate the total number of cattle on the farm
    total_cattle = 555

    # Calculate the number of cows using the ratio
    num_cows = total_cattle/(1+ratio)

    # Calculate the number of bulls by subtracting the number of cows from the total number of cattle
    num_bulls = total_cattle - num_cows

    result = num_bulls
    return result

print(solution())