def solution():
    
    years_to_get_in_shape = 2
    years_to_learn_climbing = years_to_get_in_shape * 2
    months_to_climb_each_mountain = 5
    months_to_learn_diving = 13
    years_to_dive = 2
    total_time = years_to_get_in_shape + \
        years_to_learn_climbing + (7 * months_to_climb_each_mountain) / 12 + \
        months_to_learn_diving / 12 + years_to_dive

    result = total_time
    return result

print(solution())