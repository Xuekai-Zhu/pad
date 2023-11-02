def solution():
    principle_amount = 1000
    interest_rate = 10
    time_in_years = 3
    interest = principle_amount * (interest_rate / 100) * time_in_years
    total_amount = principle_amount + interest
    result = total_amount
    return result

print(solution())