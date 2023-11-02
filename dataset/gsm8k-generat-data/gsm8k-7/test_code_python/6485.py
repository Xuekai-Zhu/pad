def solution():
    son_age_next_year = 8
    my_age_to_son_age_ratio = 5

    # Calculate son's current age
    son_age = son_age_next_year - 1

    # Calculate my current age
    my_age = son_age * my_age_to_son_age_ratio

    result = my_age
    return result

print(solution())