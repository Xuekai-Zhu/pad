def solution():
    # Find Christina's current age
    christina_half_age = 80 / 2
    christina_age_in_5_years = christina_half_age - 5
    christina_current_age = christina_age_in_5_years - 5

    # Find Oscar's current age
    oscar_age_in_15_years = (3/5) * christina_current_age + 15
    oscar_current_age = oscar_age_in_15_years - 15
    result = oscar_current_age
    return result

print(solution())