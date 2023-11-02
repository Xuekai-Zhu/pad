def solution():
    # Day 1: 50 eggs
    eggs_day1 = 50

    # Day 2: Double the production of day 1
    eggs_day2 = eggs_day1 * 2

    # Day 3: 20 more than day 2
    eggs_day3 = eggs_day2 + 20

    # Day 4: Double the total of days 1-3
    eggs_day4 = (eggs_day1 + eggs_day2 + eggs_day3) * 2

    # Total number of eggs laid
    total_eggs = eggs_day1 + eggs_day2 + eggs_day3 + eggs_day4
    result = total_eggs
    return result

print(solution())