def solution():
    emus_per_pen = 6
    num_pens = 4
    total_emus = emus_per_pen * num_pens
    female_emus = total_emus / 2
    eggs_per_day = female_emus
    eggs_per_week = eggs_per_day * 7
    result = eggs_per_week
    return result

print(solution())