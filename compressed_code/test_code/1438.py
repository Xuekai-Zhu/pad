def solution():
    
    tomato_rows = 5  
    plants_per_row = 8
    plants_per_tomato_row = plants_per_row
    plants_per_cucumber_row = plants_per_row * 2
    total_tomato_plants = tomato_rows * plants_per_tomato_row
    total_cucumber_plants = (tomato_rows * 2) * plants_per_cucumber_row  
    total_tomatoes = total_tomato_plants * 3
    result = total_tomatoes
    return result

print(solution())