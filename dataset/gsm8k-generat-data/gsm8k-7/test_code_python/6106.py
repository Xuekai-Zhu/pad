def solution():
    num_men = 8
    men_weight = 190
    num_women = 6
    women_weight = 120

    # Calculate the total weight of all men
    total_men_weight = num_men * men_weight

    # Calculate the total weight of all women
    total_women_weight = num_women * women_weight

    # Calculate the total weight of all people
    total_weight = total_men_weight + total_women_weight

    # Calculate the average weight of all people
    average_weight = total_weight / (num_men + num_women)
    result = average_weight
    return result

print(solution())