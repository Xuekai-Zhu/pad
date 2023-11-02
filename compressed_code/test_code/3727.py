def solution():
    
    last_year_cost = 250
    deposit = 0.1 * (last_year_cost * 1.4)
    remaining_cost = (last_year_cost * 1.4) - deposit
    result = remaining_cost
    return result

print(solution())