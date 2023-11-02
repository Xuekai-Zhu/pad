def solution():
    black_and_white_cost = 160
    color_cost_multiplier = 1.5

    # Calculate the cost of a color drawing
    color_cost = black_and_white_cost * color_cost_multiplier

    result = color_cost
    return result

print(solution())