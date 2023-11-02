def solution():
    toothpaste_weight = 105
    dad_use = 3
    mom_use = 2
    anne_and_brother_use = 1
    num_people = 4
    brush_times = 3

    # Calculate the total grams used per day by the family
    total_grams_used_per_day = (dad_use + mom_use + anne_and_brother_use * 2) * num_people * brush_times

    # Calculate the number of days until the toothpaste runs out
    num_days_until_empty = toothpaste_weight / total_grams_used_per_day
    result = num_days_until_empty
    return result

print(solution())