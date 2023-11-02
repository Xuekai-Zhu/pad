def solution():
    initial_number_of_bees = 80000
    target_number_of_bees = initial_number_of_bees / 4
    bees_lost_per_day = 1200

    days_to_reach_target = (initial_number_of_bees - target_number_of_bees) / bees_lost_per_day
    result = days_to_reach_target
    return result

print(solution())