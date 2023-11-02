def solution():
    # Time it takes to repair the first three cars
    time_first_three_cars = 3 * 40  # 3 cars take 40 minutes each

    # Time it takes to repair the remaining cars (50% longer)
    time_remaining_cars = 2 * (40 * 1.5)  # 2 cars take 50% longer than the first 3

    # Total time spent repairing all cars (in hours)
    total_time = (time_first_three_cars + time_remaining_cars) / 60

    # Calculate John's earnings
    earnings = total_time * 20  # John makes $20 per hour

    result = earnings
    return result

print(solution())