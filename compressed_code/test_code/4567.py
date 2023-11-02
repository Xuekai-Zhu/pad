def solution():
    
    first_plant_tomatoes = 24
    second_plant_tomatoes = (0.5 * first_plant_tomatoes) + 5
    third_plant_tomatoes = second_plant_tomatoes + 2
    total_tomatoes = first_plant_tomatoes + second_plant_tomatoes + third_plant_tomatoes
    result = total_tomatoes
    return result

print(solution())