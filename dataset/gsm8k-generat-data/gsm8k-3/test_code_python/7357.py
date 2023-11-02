def solution():
    """Jason is making sand art. He wants to fill a rectangular patch 6 inches by 7 inches with blue sand, and a square path 5 inches by 5 inches with red sand. If it takes 3 grams of sand to fill one square inch, how many grams of sand does Jason need?"""
    # Define the dimensions of the rectangular patch and the square patch
    LENGTH_RECTANGLE = 6
    WIDTH_RECTANGLE = 7
    LENGTH_SQUARE = 5

    # Calculate the areas of the rectangular patch and the square patch
    area_rectangle = LENGTH_RECTANGLE * WIDTH_RECTANGLE
    area_square = LENGTH_SQUARE ** 2

    # Calculate the total amount of sand needed in grams
    total_sand = (area_rectangle + area_square) * 3

    # Display the total amount of sand needed
    result = total_sand
    return result

print(solution())