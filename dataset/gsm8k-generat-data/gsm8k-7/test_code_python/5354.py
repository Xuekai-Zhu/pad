def solution():
    num_carrots_bed1 = 55
    num_carrots_bed2 = 101
    num_carrots_bed3 = 78
    carrots_per_pound = 6

    # Calculate the total number of carrots harvested
    total_carrots = num_carrots_bed1 + num_carrots_bed2 + num_carrots_bed3

    # Calculate the total weight of the carrots in pounds
    total_weight = total_carrots / carrots_per_pound
    result = total_weight
    return result

print(solution())