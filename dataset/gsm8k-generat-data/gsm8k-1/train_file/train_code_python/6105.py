def solution():
    """There are 8 men at a yoga studio with an average weight of 190 pounds and 6 women with an average weight of 120 pounds. What is the average weight of all 14 men and women?"""
    num_men = 8
    men_weight = 190
    num_women = 6
    women_weight = 120
    total_weight = (num_men * men_weight) + (num_women * women_weight)
    average_weight = total_weight / (num_men + num_women)
    result = average_weight
    return result

print(solution())