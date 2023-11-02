def solution():
    total_apples = 200
    rotten_percent = 0.40
    rotten_apples = total_apples * rotten_percent
    smelled_percent = 0.70
    smelled_apples = rotten_apples * smelled_percent

    # Calculate the number of rotten apples that did not smell
    not_smelled_apples = rotten_apples - smelled_apples
    result = not_smelled_apples
    return result

print(solution())