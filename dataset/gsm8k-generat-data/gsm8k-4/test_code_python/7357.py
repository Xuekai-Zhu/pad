def solution():
    """Jason is making sand art. He wants to fill a rectangular patch 6 inches by 7 inches with blue sand, and a square path 5 inches by 5 inches with red sand. If it takes 3 grams of sand to fill one square inch, how many grams of sand does Jason need?"""
    # Calculate the area of the rectangular patch
    rect_area = 6 * 7

    # Calculate the area of the square patch
    square_area = 5 * 5

    # Calculate the total area to be filled with sand
    total_area = rect_area + square_area

    # Calculate the total amount of sand needed in grams
    sand_needed = total_area * 3

    # return the result
    result = sand_needed
    return result

print(solution())