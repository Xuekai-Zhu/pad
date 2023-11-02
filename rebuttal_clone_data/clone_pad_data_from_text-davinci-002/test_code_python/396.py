def solution():
    insulin_per_day = 2
    blood_pressure_per_day = 3
    anticonvulsants_per_day = blood_pressure_per_day * 2
    days_per_week = 7
    total_pills = insulin_per_day * days_per_week + blood_pressure_per_day * days_per_week + anticonvulsants_per_day * days_per_week
    result = total_pills
    return result

print(solution())