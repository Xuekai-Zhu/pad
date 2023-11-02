def solution():
    
    initial_value = 20000
    depreciation_per_year = 1000
    years = 6
    final_value = initial_value - (depreciation_per_year * years)
    result = final_value
    return result

print(solution())