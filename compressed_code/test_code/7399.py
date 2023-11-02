def solution():
    
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