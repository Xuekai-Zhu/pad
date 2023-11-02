def solution():
    
    pie_cost_pfennigs = 2
    total_farthings = 54
    farthings_per_pfennig = 6
    total_pfennigs = total_farthings // farthings_per_pfennig
    remaining_pfennigs = total_pfennigs - pie_cost_pfennigs
    result = remaining_pfennigs
    return result

print(solution())