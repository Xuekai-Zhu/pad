def solution():
    plants = 4
    first_plant_tomatoes = 8
    second_plant_tomatoes = first_plant_tomatoes + 4
    third_plant_tomatoes = (first_plant_tomatoes + second_plant_tomatoes) * 3
    fourth_plant_tomatoes = (first_plant_tomatoes + second_plant_tomatoes) * 3

    # Calculate the total number of tomatoes
    total_tomatoes = first_plant_tomatoes + second_plant_tomatoes + third_plant_tomatoes + fourth_plant_tomatoes
    result = total_tomatoes
    return result

print(solution())