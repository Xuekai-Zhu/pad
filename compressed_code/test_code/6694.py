def solution():
    
    starting_water = 40
    water_loss_per_hour = 2
    water_added_hour_3 = 1
    water_added_hour_4 = 3
    total_water_loss = water_loss_per_hour * 4
    total_water_added = water_added_hour_3 + water_added_hour_4
    final_water_amount = starting_water - total_water_loss + total_water_added
    result = final_water_amount
    return result

print(solution())