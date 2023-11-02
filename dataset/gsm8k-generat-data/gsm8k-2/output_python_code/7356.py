def solution():
    """Jason is making sand art. He wants to fill a rectangular patch 6 inches by 7 inches with blue sand, and a square path 5 inches by 5 inches with red sand. If it takes 3 grams of sand to fill one square inch, how many grams of sand does Jason need?"""
    blue_sand_area = 6 * 7
    red_sand_area = 5 * 5
    total_area = blue_sand_area + red_sand_area
    sand_per_square_inch = 3
    total_sand = total_area * sand_per_square_inch
    result = total_sand
    return result

print(solution())