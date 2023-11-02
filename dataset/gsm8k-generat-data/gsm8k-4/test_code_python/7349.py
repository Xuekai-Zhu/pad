def solution():
    """Kara mixes cups of sugar and water in the ratio of 1:2 to make one liter of lemonade. Calculate the total number of cups of sugar used if she used 84 cups to make lemonade."""
    # Define the ratio of cups of sugar to cups of water
    sugar_to_water_ratio = 1 / 2

    # Calculate the total number of cups of sugar and water needed to make one liter of lemonade
    total_cups = 1 / (sugar_to_water_ratio + 1)

    # Calculate the number of cups of sugar needed to make one liter of lemonade
    sugar_cups_per_liter = total_cups * sugar_to_water_ratio

    # Calculate the total number of cups of sugar used to make 84 cups of lemonade
    total_sugar_cups = sugar_cups_per_liter * 84

    # return the result
    result = total_sugar_cups
    return result

print(solution())