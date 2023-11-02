def solution():
    times_per_week = 4  # Tom dances 4 times a week
    hours_per_time = 2  # Tom dances for 2 hours at a time
    weeks_per_year = 52  # There are 52 weeks in a year
    years = 10  # Tom has been dancing for 10 years

    # Calculate the total number of hours Tom danced
    total_hours = times_per_week * hours_per_time * weeks_per_year * years
    result = total_hours
    return result

print(solution())