def solution():
    watermelons_bought = 30
    watermelons_eaten = 3
    watermelons_given = 2
    watermelons_left = watermelons_bought - watermelons_eaten - watermelons_given
    weekly_consumption = watermelons_eaten + watermelons_given
    total_weeks = watermelons_bought / weekly_consumption
    result = total_weeks
    return result

print(solution())