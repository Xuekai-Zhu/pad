def solution():
    # Calculate the total weight of the 8 men
    total_weight_men = 8 * 190

    # Calculate the total weight of the 6 women
    total_weight_women = 6 * 120

    # Calculate the total weight of all 14 men and women
    total_weight = total_weight_men + total_weight_women

    # Calculate the average weight of all 14 men and women
    average_weight = total_weight / 14
    result = average_weight
    return result

print(solution())