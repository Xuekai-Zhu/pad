def solution():
    cars_repaired = 5
    num_slow_cars = 2  # 2 cars take 50% longer to repair
    hourly_rate = 20

    # Calculate the total time it takes to repair the 3 faster cars
    time_fast_cars = 40 * 3

    # Calculate the time it takes to repair 1 slow car (50% longer than the faster cars)
    time_slow_car = 1.5 * 40

    # Calculate the total time it takes to repair all slow cars
    time_slow_cars = time_slow_car * num_slow_cars

    # Calculate the total time it takes to repair all cars
    total_time = time_fast_cars + time_slow_cars

    # Calculate John's total earnings
    earnings = (total_time / 60) * hourly_rate
    result = earnings
    return result

print(solution())