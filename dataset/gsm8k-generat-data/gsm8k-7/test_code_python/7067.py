def solution():
    blue_percentage = 0.7
    red_percentage = 0.2
    white_percentage = 1 - blue_percentage - red_percentage
    blue_paint = 140

    # Calculate the total paint mixture in ounces
    total_paint = blue_paint / blue_percentage

    # Calculate the amount of white paint needed
    white_paint = total_paint * white_percentage

    result = white_paint
    return result

print(solution())