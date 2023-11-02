def solution():
    initial_amount = 1000
    interest_rate_1 = 20
    interest_rate_2 = 15
    amount_after_year_1 = initial_amount + (initial_amount * (interest_rate_1 / 100))
    tv_cost = amount_after_year_1 / 2
    remaining_amount = amount_after_year_1 - tv_cost
    amount_after_year_2 = remaining_amount + (remaining_amount * (interest_rate_2 / 100))
    result = amount_after_year_2
    
    return result

print(solution())