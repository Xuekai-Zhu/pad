def solution():
    # Calculate the time it takes to repair the first 3 cars
    time_first_three_cars = 3 * 40

    # Calculate the time it takes to repair the remaining 2 cars, which take 50% longer
    time_remaining_cars = 2 * 40 * 1.5

    # Calculate the total time for all 5 cars
    total_time = time_first_three_cars + time_remaining_cars

    # Convert the total time to hours and calculate John's earnings
    earnings = total_time / 60 * 20

    result = earnings
    return result

print(solution())