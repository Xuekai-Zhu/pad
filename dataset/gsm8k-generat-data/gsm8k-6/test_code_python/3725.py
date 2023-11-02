def solution():
    # Calculate the cost of the first 15 pounds of peanuts
    first_15_pounds_cost = 15 * 3  

    # Calculate the pounds of peanuts purchased over the minimum
    pounds_over_minimum = (105 - first_15_pounds_cost) / 3  

    result = pounds_over_minimum
    return result

print(solution())