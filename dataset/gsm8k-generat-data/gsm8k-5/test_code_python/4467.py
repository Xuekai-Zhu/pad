def solution():
    cost_of_green_lettuce = 8  # Julie spends $8 on green lettuce
    cost_of_red_lettuce = 6  # Julie spends $6 on red lettuce
    cost_per_pound = 2  # Each type of lettuce costs $2 per pound

    # Calculate the total weight of green lettuce
    weight_of_green_lettuce = cost_of_green_lettuce // cost_per_pound

    # Calculate the total weight of red lettuce
    weight_of_red_lettuce = cost_of_red_lettuce // cost_per_pound

    # Calculate the total weight of lettuce bought by Julie
    total_weight_of_lettuce = weight_of_green_lettuce + weight_of_red_lettuce
    result = total_weight_of_lettuce
    return result

print(solution())