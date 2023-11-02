def solution():
    """Phyllis has two gardens. In the first garden, she has 20 plants and 10% are tomato plants. In the second garden, she has 15 plants and 1/3 of these plants are tomato plants. What percentage of all the plants in her two gardens are tomato plants?"""
    # Calculate the number of tomato plants in the first garden
    first_garden_tomato_plants = 0.1 * 20

    # Calculate the number of tomato plants in the second garden
    second_garden_tomato_plants = (1/3) * 15

    # Calculate the total number of plants in both gardens
    total_plants = 20 + 15

    # Calculate the total number of tomato plants in both gardens
    total_tomato_plants = first_garden_tomato_plants + second_garden_tomato_plants

    # Calculate the percentage of all the plants that are tomato plants
    percentage_of_tomato_plants = (total_tomato_plants / total_plants) * 100

    # Display the percentage of tomato plants
    result = percentage_of_tomato_plants
    return result

print(solution())