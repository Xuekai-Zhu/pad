def solution():
    """Marla is mixing a particular shade of lilac that's 70% blue paint, 20% red paint, and the rest white paint. If she adds 140 ounces of blue paint, how many ounces of white paint does she add?"""
    # Define the percentages of each color
    BLUE_PERCENT = 0.7
    RED_PERCENT = 0.2
    WHITE_PERCENT = 0.1

    # Define the amount of blue paint added
    blue_paint = 140

    # Calculate the total amount of paint needed
    total_paint = blue_paint / BLUE_PERCENT

    # Calculate the amount of red paint needed
    red_paint = total_paint * RED_PERCENT

    # Calculate the amount of white paint needed
    white_paint = total_paint * WHITE_PERCENT

    # Display the amount of white paint needed
    result = white_paint
    return result

print(solution())