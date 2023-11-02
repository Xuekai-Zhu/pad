def solution():
    men = 8
    women = 6
    average_men_weight = 190
    average_women_weight = 120
    total_average_weight = (men * average_men_weight + women * average_women_weight) / (men + women)
    result = total_average_weight
    return result

print(solution())