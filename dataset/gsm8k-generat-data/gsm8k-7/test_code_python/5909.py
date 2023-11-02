def solution():
    num_cars = 2
    num_wheels_per_car = 4

    num_bikes = 2
    num_wheels_per_bike = 2

    num_wheels_per_trash_can = 2

    num_wheels_per_tricycle = 3
    num_wheels_per_roller_skates = 8  # assume the roller skates have 4 wheels each

    total_wheels = (num_cars * num_wheels_per_car) + (num_bikes * num_wheels_per_bike) + \
                   num_wheels_per_trash_can + num_wheels_per_tricycle + num_wheels_per_roller_skates
    result = total_wheels
    return result

print(solution())