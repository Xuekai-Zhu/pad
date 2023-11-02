def solution():
    starting_supplies = 400
    used_day1 = starting_supplies * (2/5)
    remaining_day1 = starting_supplies - used_day1
    used_day2 = remaining_day1 * (3/5)
    remaining_day3 = remaining_day1 - used_day2
    result = remaining_day3
    return result

print(solution())