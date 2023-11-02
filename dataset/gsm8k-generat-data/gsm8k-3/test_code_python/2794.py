def solution():
    """John repairs 5 cars.  3 of the cars take 40 minutes each to repair.  The remaining ones take 50% longer each to repair.  He makes $20 per hour repairing cars.  How much money does he make?"""
    # Define the time it takes to repair the first 3 cars
    time_first_three = 3 * 40 / 60  # convert to hours

    # Define the time it takes to repair the remaining 2 cars
    time_remaining = time_first_three * 1.5

    # Define the total time it takes to repair all 5 cars
    total_time = time_first_three + time_remaining

    # Define the hourly wage
    wage_per_hour = 20

    # Calculate the total amount of money John makes
    total_money = total_time * wage_per_hour

    # Display the total amount of money John makes
    result = total_money
    return result

print(solution())