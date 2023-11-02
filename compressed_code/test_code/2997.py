def solution():
    
    caps_per_year = [3, 5, 5, 5, 5]  
    christmas_caps = 40
    lost_caps_per_year = 15
    total_caps = 0
    for i in range(5):
        year_caps = caps_per_year[i] * 12 + christmas_caps - lost_caps_per_year
        total_caps += year_caps

    result = total_caps
    return result

print(solution())