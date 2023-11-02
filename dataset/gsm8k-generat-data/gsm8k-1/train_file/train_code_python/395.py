def solution():
    """Holly needs to take 2 insulin pills per day, 3 blood pressure pills per day, and twice as many anticonvulsants as blood pressure pills each day. How many pills does Holly take in a week?"""
    insulin_pills = 2
    blood_pressure_pills = 3
    anticonvulsant_pills = 2 * blood_pressure_pills
    pills_per_day = insulin_pills + blood_pressure_pills + anticonvulsant_pills
    total_pills = pills_per_day * 7
    result = total_pills
    return result

print(solution())