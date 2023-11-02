def solution():
    first_hour_mins = 60
    first_hour_pots = first_hour_mins / 6

    remaining_mins = 11 * 60
    warm_mins = remaining_mins - first_hour_mins
    warm_pots = warm_mins / 5

    additional_pots = warm_pots - first_hour_pots
    result = additional_pots
    return result

print(solution())