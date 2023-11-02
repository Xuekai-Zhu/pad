def solution():
    """Out of the 200 apples in an orchard, 40 percent were rotten. Also, 70 percent of the rotten apples smelled. How many rotten apples in the orchard did not smell?"""
    # Define the total number of apples and the percentage that were rotten
    total_apples = 200
    rotten_percentage = 0.4

    # Calculate the number of rotten apples
    rotten_apples = total_apples * rotten_percentage

    # Calculate the number of rotten apples that smelled
    smelled_apples = rotten_apples * 0.7

    # Calculate the number of rotten apples that did not smell
    not_smelled_apples = rotten_apples - smelled_apples

    # return the result
    result = not_smelled_apples
    return result

print(solution())