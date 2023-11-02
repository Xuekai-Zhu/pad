def solution():
    
    total_cases = 4
    shelves_per_case = 3
    records_per_shelf = 20
    total_records = total_cases * shelves_per_case * records_per_shelf * 0.6
    total_ridges = total_records * 60
    result = total_ridges
    return result

print(solution())