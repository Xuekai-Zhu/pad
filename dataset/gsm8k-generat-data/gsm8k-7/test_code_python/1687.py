def solution():
    max_load = 900
    bag_mass = 8
    num_bags = 100

    # Calculate the total mass of the bags of lemons
    total_mass = bag_mass * num_bags

    # Calculate the remaining load capacity of the truck
    remaining_load = max_load - total_mass
    result = remaining_load
    return result

print(solution())