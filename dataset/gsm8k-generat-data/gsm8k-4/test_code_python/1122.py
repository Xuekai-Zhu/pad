def solution():
    """Tim used to run 3 times a week but decided to add an extra 2 days a week.
    She runs 1 hour in the morning and 1 in the evening every day she runs.
    How many hours a week does she run now?"""
    # Define the initial number of running days per week
    initial_running_days = 3

    # Define the additional running days per week
    additional_running_days = 2

    # Calculate the total number of running days per week
    total_running_days = initial_running_days + additional_running_days

    # Calculate the total number of hours Tim runs per day
    total_running_hours_per_day = 2

    # Calculate the total number of running hours per week
    total_running_hours_per_week = total_running_days * total_running_hours_per_day

    result = total_running_hours_per_week
    return result

print(solution())