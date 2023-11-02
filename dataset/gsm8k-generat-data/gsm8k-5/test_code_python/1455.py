def solution():
    # Calculate the number of tomato plants in the first garden
    num_tomato_1 = 0.1 * 20  # 10% of 20 plants

    # Calculate the number of tomato plants in the second garden
    num_tomato_2 = (1/3) * 15  # 1/3 of 15 plants

    # Calculate the total number of plants in both gardens
    total_plants = 20 + 15

    # Calculate the total number of tomato plants
    total_tomato_plants = num_tomato_1 + num_tomato_2

    # Calculate the percentage of all plants that are tomato plants
    percent_tomato = (total_tomato_plants / total_plants) * 100
    result = percent_tomato
    return result

print(solution())