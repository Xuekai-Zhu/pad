def solution():
    num_regular_bikes = 7
    num_children_bikes = 11

    wheels_per_regular_bike = 2
    wheels_per_children_bike = 4

    total_wheels = (num_regular_bikes * wheels_per_regular_bike) + (num_children_bikes * wheels_per_children_bike)
    result = total_wheels
    return result

print(solution())