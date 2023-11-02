def solution():
    
    tomato_rows = 5  
    cucumber_rows = 10  
    plants_per_tomato_row = 8
    total_tomato_plants = tomato_rows * plants_per_tomato_row
    tomatoes_per_plant = 3
    total_tomatoes = total_tomato_plants * tomatoes_per_plant
    result = total_tomatoes
    return result

print(solution())