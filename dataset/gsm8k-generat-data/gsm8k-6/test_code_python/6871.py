def solution():
    # Calculate the total number of female emus and eggs laid per week
    females_per_pen = 6 * 0.5  # half the emus in each pen are female
    eggs_per_day = females_per_pen * 1  # each female emu lays 1 egg per day
    eggs_per_week = eggs_per_day * 7  # there are 7 days in a week
    total_eggs = eggs_per_week * 4  # John has 4 emu pens
    result = total_eggs
    return result

print(solution())