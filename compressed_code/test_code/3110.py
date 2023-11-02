def solution():
    
    dose = 1000
    interval = 6 
    duration = 14 
    pills_per_dose = dose / 500
    doses_per_day = 24 / interval
    total_doses = doses_per_day * duration
    total_pills = total_doses * pills_per_dose
    result = total_pills
    return result

print(solution())