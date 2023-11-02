def solution():
    
    daily_bottles = 0.5
    bottles_per_case = 24
    days = 240
    cases_needed = (daily_bottles * days) / bottles_per_case
    case_price = 12
    total_cost = cases_needed * case_price
    result = total_cost
    return result

print(solution())