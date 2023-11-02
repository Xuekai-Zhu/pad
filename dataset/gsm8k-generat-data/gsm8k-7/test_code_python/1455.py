def solution():
    first_garden_plants = 20
    first_garden_tomato_percentage = 0.1

    second_garden_plants = 15
    second_garden_tomato_fraction = 1/3

    # Calculate the number of tomato plants in the first garden
    first_garden_num_tomato = first_garden_plants * first_garden_tomato_percentage

    # Calculate the number of tomato plants in the second garden
    second_garden_num_tomato = second_garden_plants * second_garden_tomato_fraction

    # Calculate the total number of plants
    total_plants = first_garden_plants + second_garden_plants

    # Calculate the total number of tomato plants
    total_tomato = first_garden_num_tomato + second_garden_num_tomato

    # Calculate the percentage of all plants that are tomato plants
    tomato_percentage = (total_tomato / total_plants) * 100
    result = tomato_percentage
    return result

print(solution())