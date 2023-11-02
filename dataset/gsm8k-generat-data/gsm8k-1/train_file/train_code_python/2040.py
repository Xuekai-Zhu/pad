def solution():
    """Tony has a bucket that holds 2 pounds of sand. He has a sandbox out back that is two feet deep, four feet wide, and 5 feet long. A cubic foot of sand weighs 3 pounds. Because it's hot outside, he wants to make sure he stays hydrated, so every 4 trips he takes he drinks 3 ounces of bottled water. A 15 ounce bottle of water costs $2. He has $10 with him. How much change will he have after he buys all the water he needs?"""
    bucket_capacity = 2
    sandbox_depth = 2
    sandbox_width = 4
    sandbox_length = 5
    sand_volume = sandbox_depth * sandbox_width * sandbox_length
    sand_weight = sand_volume * 3
    trips_before_water = 4
    water_per_trip = 3
    water_bottle_size = 15
    water_bottle_price = 2
    money_available = 10
    water_needed = (sand_weight / bucket_capacity) // trips_before_water * water_per_trip
    water_cost = (water_needed / water_bottle_size) * water_bottle_price
    change = money_available - water_cost
    result = change
    return result

print(solution())