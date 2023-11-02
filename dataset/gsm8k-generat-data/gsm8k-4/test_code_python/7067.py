def solution():
    """Marla is mixing a particular shade of lilac that's 70% blue paint, 20% red paint, and the rest white paint. If she adds 140 ounces of blue paint, how many ounces of white paint does she add?"""
    # Define the percentages of blue and red paint in the final mix
    blue_percentage = 0.7
    red_percentage = 0.2

    # Calculate the remaining percentage for white paint
    white_percentage = 1 - blue_percentage - red_percentage

    # Calculate the amount of white paint needed to make up the remaining percentage
    blue_ounces = 140
    white_ounces = (blue_ounces / blue_percentage) * white_percentage

    # Return the result
    result = white_ounces
    return result

print(solution())