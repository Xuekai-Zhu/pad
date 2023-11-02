def solution():
    # Calculate the number of wrapping paper rolls Harold needs to wrap all the boxes
    rolls_for_shirt_boxes = 20/5  # 5 shirt boxes can be wrapped with one roll of wrapping paper
    rolls_for_XL_boxes = 12/3  # 3 XL boxes can be wrapped with one roll of wrapping paper
    total_rolls = rolls_for_shirt_boxes + rolls_for_XL_boxes

    # Calculate the total cost of the wrapping paper
    cost_per_roll = 4.00
    total_cost = total_rolls * cost_per_roll
    result = total_cost
    return result

print(solution())