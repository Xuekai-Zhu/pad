def solution():
    """Phyllis has two gardens. In the first garden, she has 20 plants and 10% are tomato plants. In the second garden, she has 15 plants and 1/3 of these plants are tomato plants. What percentage of all the plants in her two gardens are tomato plants?"""
    garden1_plants = 20
    garden1_tomatoes = garden1_plants * 0.1
    garden2_plants = 15
    garden2_tomatoes = garden2_plants * (1/3)
    total_plants = garden1_plants + garden2_plants
    total_tomatoes = garden1_tomatoes + garden2_tomatoes
    percent_tomatoes = (total_tomatoes / total_plants) * 100
    result = percent_tomatoes
    return result

print(solution())