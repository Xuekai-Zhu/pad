def solution():
    
    total_tvs = 40
    smart_tvs = total_tvs / 4
    analog_tvs = total_tvs / 8
    oled_tvs = total_tvs - smart_tvs - analog_tvs
    result = oled_tvs
    return result

print(solution())