def solution():
    initial_hours = 2
    increase_percent = 150
    initial_pages_per_day = 100
    days_in_week = 7

    # Calculate the new number of hours Mark spends reading per day
    new_hours = initial_hours * (1 + increase_percent/100)

    # Calculate the new number of pages Mark reads per day
    new_pages_per_day = initial_pages_per_day * (new_hours/initial_hours)

    # Calculate the new number of pages Mark reads per week
    new_pages_per_week = new_pages_per_day * days_in_week
    result = new_pages_per_week
    return result

print(solution())