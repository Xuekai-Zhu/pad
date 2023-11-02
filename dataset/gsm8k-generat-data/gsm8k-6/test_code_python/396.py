def solution():
    # Calculate the total number of pills Holly takes in a week
    insulin_pills_per_day = 2
    blood_pressure_pills_per_day = 3
    anticonvulsants_pills_per_day = 2 * blood_pressure_pills_per_day

    total_pills_per_day = insulin_pills_per_day + blood_pressure_pills_per_day + anticonvulsants_pills_per_day
    total_pills_per_week = total_pills_per_day * 7

    result = total_pills_per_week
    return result

print(solution())