def solution():
    peanut_weight = 20
    oil_to_peanut_ratio = 2/8

    # Calculate the weight of peanuts Sonja used
    peanut_used = peanut_weight / (1 + oil_to_peanut_ratio)

    # Calculate the weight of oil Sonja used
    oil_used = peanut_used * oil_to_peanut_ratio
    result = oil_used
    return result

print(solution())