def solution():
    coals_to_ash = 15
    minutes_per_bag = 20
    bags_of_coals = 3
    total_coals = bags_of_coals * 60
    total_minutes = total_coals / coals_to_ash
    result = total_minutes
    return result

print(solution())