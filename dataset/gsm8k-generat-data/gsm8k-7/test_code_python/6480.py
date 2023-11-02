def solution():
    total_mugs = 40
    total_colors = 4
    blue_ratio = 3
    yellow_mugs = 12
    red_ratio = 0.5

    # Calculate the total number of red mugs
    red_mugs = yellow_mugs * red_ratio

    # Calculate the total number of blue mugs
    blue_mugs = red_mugs * blue_ratio

    # Calculate the total number of mugs that are not red or blue or yellow
    other_mugs = total_mugs - (red_mugs + blue_mugs + yellow_mugs)

    result = other_mugs
    return result

print(solution())