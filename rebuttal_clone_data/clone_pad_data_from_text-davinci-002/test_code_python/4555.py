def solution():
    chocolate_eggs = 40
    eggs_eaten_per_day = 2
    days_in_week = 7
    eggs_eaten_per_week = days_in_week * eggs_eaten_per_day
    total_weeks = chocolate_eggs / eggs_eaten_per_week
    result = total_weeks
    return result

print(solution())