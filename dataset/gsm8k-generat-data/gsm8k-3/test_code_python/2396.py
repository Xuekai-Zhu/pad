def solution():
    """Carrie is making punch. She adds 6 12-oz cans of Mountain Dew, 28 oz of ice, and a 40 oz bottle of fruit juice. How many 10 oz servings of punch does Carrie have?"""
    # Define the amounts of each ingredient in ounces
    MOUNTAIN_DEW = 6 * 12
    ICE = 28
    FRUIT_JUICE = 40

    # Calculate the total volume of the punch
    total_volume = MOUNTAIN_DEW + ICE + FRUIT_JUICE

    # Calculate the number of 10 oz servings of punch
    servings = total_volume // 10

    # Display the number of servings
    result = servings
    return result

print(solution())