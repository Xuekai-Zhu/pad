def solution():
    # Calculate the number of sun salutations per weekday
    sun_salutations_per_weekday = 5

    # Calculate the number of weekdays in a year
    weekdays_per_year = 365 - 104  # assuming Summer takes off 2 days per week (104 days per year)

    # Calculate the total number of sun salutations in a year
    total_sun_salutations = sun_salutations_per_weekday * weekdays_per_year

    # Return the result
    return total_sun_salutations

print(solution())