def solution():
    pounds = 42
    euros = 11
    yen = 3000
    yen_per_pound = 100
    pounds_per_euro = 2
    yen_value = pounds * yen_per_pound + euros * pounds_per_euro * yen_per_pound
    result = yen_value
    
    return result

print(solution())