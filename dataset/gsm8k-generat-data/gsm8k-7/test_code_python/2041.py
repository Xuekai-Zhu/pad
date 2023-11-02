def solution():
    bucket_capacity = 2  # in pounds
    sandbox_depth = 2  # in feet
    sandbox_width = 4  # in feet
    sandbox_length = 5  # in feet
    sand_weight_per_cubic_foot = 3  # in pounds
    trips_between_drinking_water = 4
    water_bottle_size = 15  # in ounces
    water_cost_per_bottle = 2
    budget = 10  # in dollars

    # Calculate the total volume of sand needed for the sandbox
    sandbox_volume = sandbox_depth * sandbox_width * sandbox_length

    # Convert sandbox volume to cubic feet and calculate the total weight of sand needed
    sand_weight = sandbox_volume / 12 * sand_weight_per_cubic_foot

    # Calculate the total number of trips Tony needs to take to fill the bucket with sand
    num_trips = sand_weight / bucket_capacity

    # Calculate the total number of water bottles Tony needs to drink
    num_water_bottles = num_trips // trips_between_drinking_water + 1

    # Calculate the total cost of all water bottles that Tony needs to buy
    water_cost = num_water_bottles * water_cost_per_bottle

    # Calculate the change that Tony will have after buying all the water bottles
    change = budget - water_cost
    result = change
    return result

print(solution())