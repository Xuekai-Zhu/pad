def solution():
    # Calculate the weight at 9 weeks old
    weight_9_weeks = 6 * 2

    # Calculate the weight at 3 months old
    weight_3_months = weight_9_weeks * 2

    # Calculate the weight at 5 months old
    weight_5_months = weight_3_months * 2

    # Calculate the weight at 1 year old
    adult_weight = weight_5_months + 30

    result = adult_weight
    return result

print(solution())