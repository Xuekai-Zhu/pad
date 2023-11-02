def solution():
    num_guests = 40
    num_cars = 10
    cars_wheels_each = 4
    parents_cars_wheels = 8

    # Calculate the total number of car wheels in the parking lot
    total_car_wheels = (num_cars * cars_wheels_each) + parents_cars_wheels

    result = total_car_wheels
    return result

print(solution())