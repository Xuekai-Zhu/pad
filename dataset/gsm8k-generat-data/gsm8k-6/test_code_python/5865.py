def solution():
    # Calculate the number of rotten apples in the orchard
    rotten_apples = 0.4 * 200

    # Calculate the number of rotten apples that smelled
    smelled_apples = 0.7 * rotten_apples

    # Calculate the number of rotten apples that did not smell
    not_smelled_apples = rotten_apples - smelled_apples

    result = not_smelled_apples
    return result

print(solution())