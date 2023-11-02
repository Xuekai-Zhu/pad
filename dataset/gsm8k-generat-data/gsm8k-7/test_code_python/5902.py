def solution():
    # Calculate number of tomatoes from first plant
    first_plant_tomatoes = 24

    # Calculate number of tomatoes from second plant
    second_plant_tomatoes = (first_plant_tomatoes / 2) + 5

    # Calculate number of tomatoes from third plant
    third_plant_tomatoes = second_plant_tomatoes + 2

    # Calculate total number of tomatoes
    total_tomatoes = first_plant_tomatoes + second_plant_tomatoes + third_plant_tomatoes

    result = total_tomatoes
    return result

print(solution())