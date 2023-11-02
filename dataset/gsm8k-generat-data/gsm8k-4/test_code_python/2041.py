def solution():
    """Tony has a bucket that holds 2 pounds of sand. He has a sandbox out back that is two feet deep, four feet wide, and 5 feet long. A cubic foot of sand weighs 3 pounds. Because it's hot outside, he wants to make sure he stays hydrated, so every 4 trips he takes he drinks 3 ounces of bottled water. A 15 ounce bottle of water costs $2. He has $10 with him. How much change will he have after he buys all the water he needs?"""
    # Calculate the volume of the sandbox in cubic feet
    sandbox_volume = 2 * 4 * 5

    # Calculate the weight of sand needed to fill the sandbox
    sand_weight = sandbox_volume * 3

    # Calculate the number of trips needed to fill the bucket with sand
    trips = sand_weight // 2 + (sand_weight % 2 > 0)

    # Calculate the number of bottles of water needed based on the number of trips
    water_bottles = trips // 4 + (trips % 4 > 0)

    # Calculate the cost of the water bottles
    water_cost = water_bottles * 2

    # Calculate the number of ounces of water Tony drinks
    water_drunk = water_bottles * 3

    # Calculate the cost of the water Tony drinks
    water_drunk_cost = (water_drunk / 15) * 2

    # Calculate the total cost of water
    total_cost = water_cost + water_drunk_cost

    # Calculate the change Tony will have
    change = 10 - total_cost

    result = change
    return result

print(solution())