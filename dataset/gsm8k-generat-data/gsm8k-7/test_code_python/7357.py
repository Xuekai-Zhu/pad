def solution():
    blue_area = 6 * 7  # area of rectangular patch
    blue_sand = blue_area * 3  # grams of blue sand needed

    red_area = 5 * 5  # area of square patch
    red_sand = red_area * 3  # grams of red sand needed

    total_sand = blue_sand + red_sand
    result = total_sand
    return result

print(solution())