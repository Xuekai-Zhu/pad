def solution():
    time_per_car_wash = 10 / 60  # 10 minutes to wash a car, converted to hours
    time_per_oil_change = 15 / 60  # 15 minutes to change oil, converted to hours
    time_per_tire_change = 30 / 60  # 30 minutes to change a set of tires, converted to hours
    num_car_washes = 9
    num_oil_changes = 6
    num_tire_changes = 2

    # Calculate the total time spent on car washes, oil changes, and tire changes
    total_time = num_car_washes * time_per_car_wash + num_oil_changes * time_per_oil_change + num_tire_changes * time_per_tire_change

    result = total_time
    return result

print(solution())