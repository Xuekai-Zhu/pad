def solution():
    # Calculate the total weight of the 8 men
    men_weight = 8 * 190

    # Calculate the total weight of the 6 women
    women_weight = 6 * 120

    # Calculate the total weight of all 14 people
    total_weight = men_weight + women_weight

    # Calculate the average weight of all 14 people
    average_weight = total_weight / 14
    result = average_weight
    return result

print(solution())