def solution():
    blue_paint_percentage = 70  # The shade of lilac is 70% blue paint
    red_paint_percentage = 20  # The shade of lilac is 20% red paint
    white_paint_percentage = 100 - blue_paint_percentage - red_paint_percentage  # The rest is white paint
    blue_paint_added = 140  # Marla adds 140 ounces of blue paint

    # Calculate the total amount of paint needed
    total_paint = blue_paint_added / (blue_paint_percentage / 100)

    # Calculate the amount of white paint needed
    white_paint_added = total_paint * (white_paint_percentage / 100)
    result = white_paint_added
    return result

print(solution())