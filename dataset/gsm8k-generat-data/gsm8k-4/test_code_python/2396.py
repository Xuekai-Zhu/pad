def solution():
    """Carrie is making punch. She adds 6 12-oz cans of Mountain Dew, 28 oz of ice, and a 40 oz bottle of fruit juice. How many 10 oz servings of punch does Carrie have?"""
    # Define the volume in ounces of Mountain Dew cans, ice, and fruit juice
    MOUNTAIN_DEW_VOLUME = 12
    ICE_VOLUME = 28
    FRUIT_JUICE_VOLUME = 40

    # Calculate the total volume in ounces of the punch
    total_volume = (6 * MOUNTAIN_DEW_VOLUME) + ICE_VOLUME + FRUIT_JUICE_VOLUME

    # Calculate the number of 10 oz servings in the punch
    servings = total_volume // 10

    # return the result
    result = servings
    return result

print(solution())