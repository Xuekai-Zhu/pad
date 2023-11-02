def solution():
    cans_of_soda = 6
    ounces_of_soda = 12
    weight_of_cans = 2
    additional_cans = 2
    total_weight = (cans_of_soda * (ounces_of_soda + weight_of_cans)) + (additional_cans * weight_of_cans)
    result = total_weight
    return result

print(solution())