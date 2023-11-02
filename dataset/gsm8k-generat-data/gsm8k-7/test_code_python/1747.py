def solution():
    mara_bags = 12
    mara_marbles_per_bag = 2
    markus_bags = 2
    markus_marbles_per_bag = 13

    # Calculate the total number of marbles Mara has
    mara_total_marbles = mara_bags * mara_marbles_per_bag

    # Calculate the total number of marbles Markus has
    markus_total_marbles = markus_bags * markus_marbles_per_bag

    # Calculate the difference in the number of marbles
    difference = markus_total_marbles - mara_total_marbles
    result = difference
    return result

print(solution())