def solution():
    truck_capacity = 900
    bag_mass = 8
    number_of_bags = 100
    total_mass = bag_mass * number_of_bags
    remaining_capacity = truck_capacity - total_mass
    result = remaining_capacity
    return result

print(solution())