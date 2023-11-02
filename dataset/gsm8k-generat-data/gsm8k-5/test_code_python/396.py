def solution():
    insulin_pills_per_day = 2  # Holly needs to take 2 insulin pills per day
    blood_pressure_pills_per_day = 3  # Holly needs to take 3 blood pressure pills per day
    anticonvulsant_pills_per_day = blood_pressure_pills_per_day * 2  # Holly needs to take twice as many anticonvulsants as blood pressure pills

    pills_per_day = insulin_pills_per_day + blood_pressure_pills_per_day + anticonvulsant_pills_per_day  # Total number of pills Holly takes per day
    pills_per_week = pills_per_day * 7  # Total number of pills Holly takes per week

    result = pills_per_week
    return result

print(solution())