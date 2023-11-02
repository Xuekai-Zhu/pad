def solution():
    water_per_dose = 4
    doses_per_day = 3
    days_per_week = 7

    total_doses_week1 = doses_per_day * days_per_week

    # For week 2, Kara missed two doses, so she only took 19 doses
    total_doses_week2 = (doses_per_day * (days_per_week - 1)) + (doses_per_day - 2)

    # Calculate the total amount of water Kara drank over both weeks
    total_water = (total_doses_week1 + total_doses_week2) * water_per_dose
    result = total_water
    return result

print(solution())