def solution():
    
    car_value = 20000
    depreciation_rate = 1000
    years_owned = 6
    value_after_depreciation = car_value - (depreciation_rate * years_owned)
    result = value_after_depreciation
    return result

print(solution())