def solution():
    # Calculate the total area of the flag
    flag_area = 5 * 4 * 2  # both sides need to be painted

    # Calculate the total amount of paint needed
    paint_needed = flag_area / 4  # 1 quart is good for 4 square feet

    # Calculate the total cost of paint
    paint_cost = paint_needed * 2  # paint costs $2 per quart

    result = paint_cost
    return result

print(solution())