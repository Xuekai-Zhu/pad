def solution():
    
    bottles_per_day = 0.5
    bottles_per_case = 24
    days_in_case = bottles_per_case / bottles_per_day
    cases_needed = 240 / days_in_case
    case_price = 12.00
    total_price = cases_needed * case_price
    result = total_price
    
    return result

print(solution())