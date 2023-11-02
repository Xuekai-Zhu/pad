def solution():
    peanut_butter_weight = 20  # Sonja's last batch of peanut butter weighed 20 ounces
    oil_to_peanuts_ratio = 2/8  # Sonja uses 2 ounces of oil for every 8 ounces of peanuts

    # Calculate the weight of peanuts in the batch
    peanut_weight = peanut_butter_weight / (1 + oil_to_peanuts_ratio)

    # Calculate the weight of oil used in the batch
    oil_weight = oil_to_peanuts_ratio * peanut_weight
    result = oil_weight
    return result

print(solution())