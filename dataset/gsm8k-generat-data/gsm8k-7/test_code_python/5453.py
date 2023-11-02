def solution():
    # Convert all times to hours
    walk_time = 5/60
    bus_time = 20/60
    total_commute_time = (2 * walk_time) + bus_time

    # Calculate the total time spent commuting per day
    total_time_per_day = 2 * total_commute_time

    # Calculate the total time spent commuting per year
    days_per_year = 365
    total_time_per_year = days_per_year * total_time_per_day

    result = total_time_per_year
    return result

print(solution())