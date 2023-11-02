def solution():
    """Kara mixes cups of sugar and water in the ratio of 1:2 to make one liter of lemonade. Calculate the total number of cups of sugar used if she used 84 cups to make lemonade."""
    # Define the ratio of cups of sugar and water to make one liter of lemonade
    SUGAR_WATER_RATIO = 1 / 2

    # Calculate the total volume of lemonade made in cups
    total_volume = 84 / SUGAR_WATER_RATIO

    # Calculate the volume of sugar used in cups
    sugar_volume = total_volume / (1 + SUGAR_WATER_RATIO)

    # Calculate the number of cups of sugar used
    cups_of_sugar = sugar_volume

    # Display the number of cups of sugar used
    result = cups_of_sugar
    return result

print(solution())