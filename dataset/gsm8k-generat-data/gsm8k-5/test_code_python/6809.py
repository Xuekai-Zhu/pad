def solution():
    payment_per_task = 40  # Jerry earns $40 per task
    time_per_task = 2  # Each task takes Jerry 2 hours to complete
    hours_per_day = 10  # Jerry works 10 hours per day
    days_per_week = 7  # Jerry works a whole week

    # Calculate the number of tasks Jerry completes in a week
    tasks_per_week = (hours_per_day * days_per_week) // time_per_task

    # Calculate the total amount of money Jerry would earn at the end of the week
    total_payment = payment_per_task * tasks_per_week
    result = total_payment
    return result

print(solution())