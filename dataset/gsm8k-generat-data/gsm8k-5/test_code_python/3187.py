def solution():
    sun_salutations_per_day = 5  # Summer performs 5 sun salutations each weekday
    weekdays_per_year = 5 * 52  # There are 5 weekdays in a week and 52 weeks in a year

    # Calculate the total number of sun salutations Summer will perform in a year
    total_sun_salutations = sun_salutations_per_day * weekdays_per_year
    result = total_sun_salutations
    return result

print(solution())