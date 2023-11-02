def solution():
    # Define the amount of sleep Tom has been getting
    weeknight_sleep = 5
    weekend_sleep = 6

    # Calculate the total amount of sleep Tom has been getting
    total_sleep = (5 * weeknight_sleep) + (2 * weekend_sleep)

    # Calculate the total amount of sleep Tom ideally wants
    ideal_sleep = 56

    # Calculate how many hours of sleep Tom is behind on
    sleep_deficit = ideal_sleep - total_sleep
    result = sleep_deficit
    return result

print(solution())