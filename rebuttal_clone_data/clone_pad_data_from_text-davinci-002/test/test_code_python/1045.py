def solution():
    rows_total = 15
    tomato_rows = rows_total / 3
    cucumber_rows = 2 * tomato_rows
    tomato_plants_per_row = 8
    tomatoes_per_plant = 3
    total_tomatoes = tomato_rows * tomato_plants_per_row * tomatoes_per_plant
    result = total_tomatoes
    return result

print(solution())