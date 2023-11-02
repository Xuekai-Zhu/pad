def solution():
    # Calculate the total number of marbles Mara has
    mara_total_marbles = 12 * 2  # 12 bags with 2 marbles in each bag
    # Calculate the total number of marbles Markus has
    markus_total_marbles = 2 * 13  # 2 bags with 13 marbles in each bag
    # Calculate the difference in the number of marbles
    marbles_diff = markus_total_marbles - mara_total_marbles
    result = marbles_diff
    return result

print(solution())