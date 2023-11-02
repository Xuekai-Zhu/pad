def solution():
    """Jason is making sand art. He wants to fill a rectangular patch 6 inches by 7 inches with blue sand, and a square path 5 inches by 5 inches with red sand. If it takes 3 grams of sand to fill one square inch, how many grams of sand does Jason need?"""
    blue_patch_area = 6 * 7
    red_patch_area = 5 * 5
    total_area = blue_patch_area + red_patch_area
    grams_per_square_inch = 3
    total_sand_needed = total_area * grams_per_square_inch
    result = total_sand_needed
    return result

print(solution())