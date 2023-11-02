def solution():
    """John repairs 5 cars. 3 of the cars take 40 minutes each to repair. The remaining ones take 50% longer each to repair. He makes $20 per hour repairing cars. How much money does he make?"""
    # Define the time it takes to repair the first set of cars
    time_1 = 40 * 3

    # Define the time it takes to repair the remaining cars
    time_2 = 1.5 * 40 * 2

    # Calculate the total time it takes to repair all the cars
    total_time = time_1 + time_2

    # Calculate the amount of money John makes based on the total time spent repairing cars
    money = (total_time / 60) * 20

    # Return the result
    result = money
    return result

print(solution())