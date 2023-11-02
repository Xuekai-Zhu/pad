def solution():
    num_kids = 4
    num_eggs_per_kid = 2
    num_eggs_husband = 3
    num_eggs_lisa = 2
    num_days_week = 5
    num_weeks_year = 52

    # Calculate total number of eggs Lisa cooks for her family in a week
    total_eggs_week = (num_kids * num_eggs_per_kid) + num_eggs_husband + num_eggs_lisa

    # Calculate total number of eggs Lisa cooks for her family in a year
    total_eggs_year = total_eggs_week * num_days_week * num_weeks_year

    result = total_eggs_year
    return result

print(solution())