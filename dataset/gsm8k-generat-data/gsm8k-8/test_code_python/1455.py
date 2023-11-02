def solution():
    # Calculate the number of tomato plants in garden 1
    garden1_tomato_plants = 0.1 * 20

    # Calculate the number of tomato plants in garden 2
    garden2_tomato_plants = (1/3) * 15

    # Calculate the total number of plants in both gardens
    total_plants = 20 + 15

    # Calculate the total number of tomato plants in both gardens
    total_tomato_plants = garden1_tomato_plants + garden2_tomato_plants

    # Calculate the percentage of tomato plants in both gardens
    percentage_tomato_plants = (total_tomato_plants / total_plants) * 100

    result = percentage_tomato_plants
    return result

print(solution())