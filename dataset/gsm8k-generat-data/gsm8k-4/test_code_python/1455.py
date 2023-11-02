def solution():
    """Phyllis has two gardens. In the first garden, she has 20 plants and 10% are tomato plants. In the second garden, she has 15 plants and 1/3 of these plants are tomato plants. What percentage of all the plants in her two gardens are tomato plants?"""
    # Calculate the number of tomato plants in the first garden
    garden1_plants = 20
    garden1_tomatoes = 0.1 * garden1_plants

    # Calculate the number of tomato plants in the second garden
    garden2_plants = 15
    garden2_tomatoes = (1/3) * garden2_plants

    # Calculate the total number of plants and tomato plants
    total_plants = garden1_plants + garden2_plants
    total_tomatoes = garden1_tomatoes + garden2_tomatoes

    # Calculate the percentage of tomato plants in both gardens
    percentage_tomatoes = (total_tomatoes / total_plants) * 100

    # Return the result
    result = percentage_tomatoes
    return result

print(solution())