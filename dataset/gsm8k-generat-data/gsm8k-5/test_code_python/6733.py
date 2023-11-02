def solution():
    flag_width = 5  # The flag is 5 feet wide
    flag_height = 4  # The flag is 4 feet tall
    surface_area = 2 * flag_width * flag_height  # The surface area of the flag

    # Calculate the amount of paint needed in quarts
    paint_quarts = surface_area / 4  # 1 quart is good for 4 square feet

    # Calculate the cost of paint
    paint_cost_per_quart = 2
    total_paint_cost = paint_quarts * paint_cost_per_quart
    result = total_paint_cost
    return result

print(solution())