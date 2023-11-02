def solution():
    pounds_per_hour = 1.5
    hours_per_day = 2
    days_per_week = 7
    weeks = 2
    total_hours = hours_per_day * days_per_week * weeks
    total_pounds = pounds_per_hour * total_hours
    kilos_per_pound = 2.2
    total_kilos = total_pounds / kilos_per_pound
    starting_weight = 80
    final_weight = starting_weight - total_kilos
    result = final_weight
    return result

print(solution())