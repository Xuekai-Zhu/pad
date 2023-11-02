def solution():
    # Total steps taken in the first 5 days
    total_steps = 9400 + 9100 + 8300 + 9200 + 8900

    # Total number of days left in the week
    days_left = 2

    # Target number of steps for the week
    target_steps = 7 * 9000

    # Number of steps Toby needs to average on Friday and Saturday
    required_steps = (target_steps - total_steps) / days_left
    result = required_steps
    return result

print(solution())