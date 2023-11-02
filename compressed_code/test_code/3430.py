def solution():
    
    cases = 15
    tins_per_case = 24
    total_tins = cases * tins_per_case
    damaged_tins = round(total_tins * 0.05)
    remaining_tins = total_tins - damaged_tins
    result = remaining_tins
    return result

print(solution())