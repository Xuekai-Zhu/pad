def solution():
    insulin_pills_per_day = 2
    blood_pressure_pills_per_day = 3
    anticonvulsants_per_day = 2 * blood_pressure_pills_per_day
    pills_per_week = (insulin_pills_per_day + blood_pressure_pills_per_day + anticonvulsants_per_day) * 7
    result = pills_per_week
    return result

print(solution())