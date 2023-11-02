def solution():
    
    pens = 4
    emus_per_pen = 6
    female_emus_per_pen = emus_per_pen / 2
    eggs_per_day = pens * female_emus_per_pen
    eggs_per_week = eggs_per_day * 7
    result = eggs_per_week
    return result

print(solution())