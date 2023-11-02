def solution():
    
    first_garden_plants = 20
    first_garden_tomatoes = 0.1 * first_garden_plants
    second_garden_plants = 15
    second_garden_tomatoes = (1/3) * second_garden_plants
    total_plants = first_garden_plants + second_garden_plants
    total_tomatoes = first_garden_tomatoes + second_garden_tomatoes
    percentage_tomatoes = (total_tomatoes / total_plants) * 100
    result = percentage_tomatoes
    return result

print(solution())