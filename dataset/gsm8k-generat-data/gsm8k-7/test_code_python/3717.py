def solution():
    num_plants_after_3_months = 20
    num_plants_given_away = 4
    num_months = 3

    # Calculate the number of plants Mark had before giving any away
    num_plants_before_3_months = num_plants_after_3_months + num_plants_given_away
    # backtrack 3 months
    num_plants_before_doubling = num_plants_before_3_months / 2 / 2 / 2
    result = int(num_plants_before_doubling)
    return result

print(solution())