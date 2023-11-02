def solution():
    lime_juice_per_mocktail = 1
    mocktails_per_day = 1
    lime_juice_per_lime = 2
    limes_per_mocktail = lime_juice_per_mocktail / lime_juice_per_lime
    limes_needed = mocktails_per_day * limes_per_mocktail
    cost_per_lime = 1 / 3
    total_cost = limes_needed * cost_per_lime
    result = total_cost
    return result

print(solution())