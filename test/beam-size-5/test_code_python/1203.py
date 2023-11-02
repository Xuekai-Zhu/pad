def solution():
    
    tunas_last_monday = 3
    tunas_first_tuna = 56
    tunas_second_tuna = 46
    tunas_last_tuna = 26
    cost_per_kilogram = 0.5
    total_weight = tunas_last_monday + tunas_first_tuna + tunas_second_tuna + tunas_last_tuna
    total_earnings = total_weight * cost_per_kilogram
    result = total_earnings
    return result

print(solution())