def solution():
    
    deposit = 2000
    interest_rate = 0.08
    time_in_years = 2.5
    total_interest = deposit * interest_rate * time_in_years
    total_amount = deposit + total_interest
    result = total_amount
    return result

print(solution())