def solution():
    flour_cups = 2  # Felicia needs 2 cups of flour
    white_sugar_cups = 1  # Felicia needs 1 cup of white sugar
    brown_sugar_cups = 0.25  # Felicia needs 1/4 cup of brown sugar
    oil_cups = 0.5  # Felicia needs 1/2 cup of oil

    # Calculate the total number of fills needed for each ingredient
    flour_fills = flour_cups / 0.25  # One fill is 1/4 cup
    white_sugar_fills = white_sugar_cups / 0.25
    brown_sugar_fills = brown_sugar_cups / 0.25
    oil_fills = oil_cups / 0.25

    # Take the maximum number of fills needed to find the total number of fills
    total_fills = max(flour_fills, white_sugar_fills, brown_sugar_fills, oil_fills)
    result = total_fills
    return result

print(solution())