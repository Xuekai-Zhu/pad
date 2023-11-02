def solution():
    num_pens = 4
    emus_per_pen = 6
    female_ratio = 0.5
    eggs_per_female = 1
    days_per_week = 7

    # Calculate the total number of female emus
    total_emus = num_pens * emus_per_pen
    females = total_emus * female_ratio

    # Calculate the total number of eggs per week
    total_eggs = females * eggs_per_female * days_per_week
    result = total_eggs
    return result

print(solution())