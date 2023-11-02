def solution():
    
    roof_capacity = 500
    leaves_per_pound = 1000
    leaves_per_day = 100
    pounds_per_day = leaves_per_day / leaves_per_pound
    days_until_collapse = roof_capacity / pounds_per_day
    result = days_until_collapse
    return result

print(solution())