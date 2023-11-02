def solution():
    cases_ordered_April = 20
    cases_ordered_May = 30
    bottles_per_case = 20
    total_bottles_April = cases_ordered_April * bottles_per_case
    total_bottles_May = cases_ordered_May * bottles_per_case
    total_bottles_ordered = total_bottles_April + total_bottles_May
    result = total_bottles_ordered
    
    return result

print(solution())