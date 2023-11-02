def solution():
    # Calculate the amount of lime juice used in 30 days
    lime_juice_used = 1 * 30  # 1 tablespoon per mocktail, made every evening for 30 days

    # Calculate the number of limes needed for the lime juice
    limes_needed = lime_juice_used / 2  # 2 tablespoons per lime

    # Calculate the cost of the limes
    cost_of_limes = (limes_needed / 3) * 1.00  # 3 limes for $1.00

    result = cost_of_limes
    return result

print(solution())