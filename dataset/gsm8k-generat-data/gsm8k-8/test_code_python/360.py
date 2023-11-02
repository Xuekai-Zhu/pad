def solution():
    # Define the ratio of oil to peanuts
    oil_to_peanuts_ratio = 2/8

    # Calculate the weight of peanuts used
    peanut_weight = 20 / (1 + oil_to_peanuts_ratio)

    # Calculate the weight of oil used
    oil_weight = oil_to_peanuts_ratio * peanut_weight

    result = oil_weight
    return result

print(solution())