def solution():
    previous_days = 3  # Tim used to run 3 times a week
    extra_days = 2  # Tim decided to add an extra 2 days a week
    total_days = previous_days + extra_days  # Tim now runs a total of 5 days a week
    hours_per_day = 2  # Tim runs 1 hour in the morning and 1 hour in the evening every day she runs

    # Calculate the total number of hours Tim now runs per week
    total_hours = total_days * hours_per_day
    result = total_hours
    return result

print(solution())