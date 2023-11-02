def solution():
    
    sand_volume = 2  
    sandbox_volume = 2 * 4 * 5  
    sand_weight = sandbox_volume * 3  
    num_bucket_trips = sand_weight // sand_volume
    num_water_bottles = (num_bucket_trips // 4) * 3
    water_cost = num_water_bottles * (2 / 15)
    total_cost = water_cost
    change = 10 - total_cost
    result = change
    return result

print(solution())