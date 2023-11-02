def solution():
    # Calculate the volume of the sandbox in cubic feet
    sandbox_volume = 2 * 4 * 5

    # Calculate the weight of one cubic foot of sand
    sand_weight = 3

    # Calculate the total weight of sand needed to fill the sandbox
    sand_weight_needed = sandbox_volume * sand_weight

    # Calculate the number of pounds of sand in each bucket
    bucket_weight = 2

    # Calculate the total number of buckets of sand needed
    buckets_needed = sand_weight_needed / bucket_weight

    # Calculate the total number of trips Tony will make
    total_trips = buckets_needed * 2

    # Calculate the number of water bottles needed
    num_water_bottles = total_trips // 4 + 1

    # Calculate the cost of the water bottles
    water_cost = num_water_bottles * 2

    # Calculate the change Tony will have
    change = 10 - water_cost
    result = change
    return result

print(solution())