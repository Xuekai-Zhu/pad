def solution():
    
    weight_per_watermelon = 23
    price_per_pound = 2
    num_watermelons = 18
    total_weight = weight_per_watermelon * num_watermelons
    total_income = total_weight * price_per_pound
    result = total_income
    return result

print(solution())