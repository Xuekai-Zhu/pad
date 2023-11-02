def solution():
    """Out of the 200 apples in an orchard, 40 percent were rotten. Also, 70 percent of the rotten apples smelled. How many rotten apples in the orchard did not smell?"""
    # Define the number of apples in the orchard and the percentage of rotten apples
    total_apples = 200
    rotten_percent = 40

    # Calculate the number of rotten apples and the number that smelled
    rotten_apples = total_apples * (rotten_percent / 100)
    smelled_rotten = rotten_apples * 0.7

    # Calculate the number of rotten apples that did not smell
    not_smelled_rotten = rotten_apples - smelled_rotten

    # Display the number of rotten apples that did not smell
    result = not_smelled_rotten
    return result

print(solution())