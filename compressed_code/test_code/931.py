def solution():
    
    initial_amount = 80
    growth_rate_1 = 0.15
    growth_rate_2 = 0.10
    amount_after_year_1 = initial_amount * (1 + growth_rate_1)
    amount_after_year_2 = (amount_after_year_1 + 28) * (1 + growth_rate_2)
    result = amount_after_year_2
    return result

print(solution())