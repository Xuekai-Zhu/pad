def solution():
    # Calculate the total amount of time John works on the 3 cars.
    time_3_cars = 3 * 40  # 3 of the cars take 40 minutes each to repair

    # Calculate the amount of time each of the remaining 2 cars takes to repair.
    time_each_remaining_car = 1.5 * 40  # the remaining ones take 50% longer each to repair

    # Calculate the total amount of time John works on the remaining 2 cars.
    time_remaining_cars = 2 * time_each_remaining_car

    # Calculate the total amount of time John works.
    total_time = time_3_cars + time_remaining_cars

    # Calculate the amount of money John makes.
    money_made = (total_time / 60) * 20  # he makes $20 per hour

    result = money_made
    return result

print(solution())