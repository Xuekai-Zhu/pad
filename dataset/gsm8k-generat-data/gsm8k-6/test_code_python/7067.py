def solution():
    # Determine the total amount of paint needed to make the lilac shade
    total_paint = 140 / 0.7  # since blue paint is 70%, total amount of paint is 140/0.7

    # Determine the amount of white paint needed
    white_paint = total_paint - 140 - 0.2*total_paint  # red paint is 20% and the rest is white paint

    result = white_paint
    return result

print(solution())