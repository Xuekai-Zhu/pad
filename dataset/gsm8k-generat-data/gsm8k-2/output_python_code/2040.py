def solution():
    """Tony has a bucket that holds 2 pounds of sand. He has a sandbox out back that is two feet deep, four feet wide, and 5 feet long. A cubic foot of sand weighs 3 pounds. Because it's hot outside, he wants to make sure he stays hydrated, so every 4 trips he takes he drinks 3 ounces of bottled water. A 15 ounce bottle of water costs $2. He has $10 with him. How much change will he have after he buys all the water he needs?"""
    sand_volume = 2  # in pounds
    sandbox_volume = 2 * 4 * 5  # in cubic feet
    sand_weight = sandbox_volume * 3  # in pounds
    num_bucket_trips = sand_weight // sand_volume
    num_water_bottles = (num_bucket_trips // 4) * 3
    water_cost = num_water_bottles * (2 / 15)
    total_cost = water_cost
    change = 10 - total_cost
    result = change
    return result

print(solution())