def solution():
    total_mushrooms = 30  # The fallen log has 30 mushrooms growing on its side
    ratio_gilled_to_spotted = 1 / 9  # For every gilled mushroom, there are 9 spotted mushrooms

    # Calculate the number of gilled mushrooms and spotted mushrooms
    gilled_mushrooms = total_mushrooms / (1 + 9)  # One gilled mushroom for every 9 spotted mushrooms
    spotted_mushrooms = total_mushrooms - gilled_mushrooms

    result = gilled_mushrooms
    return result

print(solution())