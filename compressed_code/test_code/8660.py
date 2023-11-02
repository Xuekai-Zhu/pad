def solution():
    
    savings = 2225
    rent_per_month = 1250
    months_advance = 2
    deposit = 500
    total_cost = (rent_per_month * months_advance) + deposit
    amount_needed = total_cost - savings
    result = amount_needed
    return result

print(solution())