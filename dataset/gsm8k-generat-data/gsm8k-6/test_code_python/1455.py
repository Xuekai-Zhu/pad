def solution():
    # Calculate the number of tomato plants in each garden
    garden1_tomatoes = 0.10 * 20
    garden2_tomatoes = (1/3) * 15

    # Calculate the total number of plants and tomato plants
    total_plants = 20 + 15
    total_tomatoes = garden1_tomatoes + garden2_tomatoes

    # Calculate the percentage of tomato plants
    percent_tomatoes = (total_tomatoes / total_plants) * 100
    result = percent_tomatoes
    return result

print(solution())