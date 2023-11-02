def solution():
    days_per_year = 250  # There are 250 days per year on Orbius-5
    seasons_per_year = 5  # There are 5 seasons in a year on Orbius-5
    seasons_on_orbius = 3  # The astronaut stays on Orbius-5 for 3 seasons

    # Calculate the total number of days the astronaut spends on Orbius-5
    total_days = (days_per_year / seasons_per_year) * seasons_on_orbius
    result = total_days
    return result

print(solution())