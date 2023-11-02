def solution():
    
    carwash_soap_price = 4
    bottles_needed_per_week = 1/4
    total_weeks = 20
    total_bottles = bottles_needed_per_week * total_weeks
    total_cost = total_bottles * carwash_soap_price
    result = total_cost
    return result

print(solution())