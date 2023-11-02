def solution():
    # Calculate the amount of sparkling water Mary Anne drinks in a year
    water_in_year = (1/5) * 365  # Mary Anne drinks 1/5 of a bottle every night, there are 365 nights in a year

    # Calculate the cost of the sparkling water Mary Anne drinks in a year
    cost_in_year = (water_in_year * 2)  # each bottle costs $2.00

    result = cost_in_year
    return result

print(solution())