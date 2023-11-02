def solution():
    eggs_per_day = 2
    total_eggs = 40
    days_to_last = total_eggs / eggs_per_day
    weeks_to_last = days_to_last / 7
    result = weeks_to_last
    return result

print(solution())