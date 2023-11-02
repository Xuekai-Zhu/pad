def solution():
    num_cars = 2
    num_wheels_per_car = 4

    num_lawnmowers = 1
    num_wheels_per_lawnmower = 4

    num_bicycles = 3
    num_wheels_per_bicycle = 2

    num_tricycles = 1
    num_wheels_per_tricycle = 3

    num_unicycles = 1
    num_wheels_per_unicycle = 1

    # Calculate the total number of wheels in the garage
    total_wheels = (num_cars * num_wheels_per_car) + (num_lawnmowers * num_wheels_per_lawnmower) + (num_bicycles * num_wheels_per_bicycle) + (num_tricycles * num_wheels_per_tricycle) + (num_unicycles * num_wheels_per_unicycle)
    result = total_wheels
    return result

print(solution())