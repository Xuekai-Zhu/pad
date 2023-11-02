def solution():
    """Tim used to run 3 times a week but decided to add an extra 2 days a week.  She runs 1 hour in the morning and 1 in the evening every day she runs.  How many hours a week does she run now?"""
    # Calculate the total number of days Tim now runs per week
    total_days = 3 + 2

    # Calculate the total number of hours Tim runs per day
    hours_per_day = 2

    # Calculate the total number of hours Tim now runs per week
    total_hours = total_days * hours_per_day

    # Display the total number of hours Tim runs per week
    result = total_hours
    return result

print(solution())