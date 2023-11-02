def solution():
    time_to_mow_one_line = 2
    time_to_plant_one_flower = 0.5
    lines_to_mow = 40
    rows_of_flowers = 8
    flowers_per_row = 7
    minutes_to_mow = time_to_mow_one_line * lines_to_mow
    minutes_to_plant = time_to_plant_one_flower * flowers_per_row * rows_of_flowers
    total_minutes = minutes_to_mow + minutes_to_plant
    result = total_minutes
    
    return result

print(solution())