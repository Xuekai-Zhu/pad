def solution():
    """Abigail is trying a new recipe for a cold drink. It uses 1/4 of a cup of iced tea and 1 and 1/4 of a cup of lemonade to make one drink. If she fills a pitcher with 18 total cups of this drink, how many cups of lemonade are in the pitcher?"""
    # Define the ratio of iced tea to lemonade in one drink
    ICED_TEA_RATIO = 1 / 4
    LEMONADE_RATIO = 1 + 1 / 4

    # Define the total number of drinks in the pitcher
    total_drinks = 18

    # Calculate the total amount of iced tea in the pitcher
    iced_tea_cups = total_drinks * ICED_TEA_RATIO

    # Calculate the total amount of lemonade in the pitcher
    lemonade_cups = total_drinks * LEMONADE_RATIO - iced_tea_cups

    # Display the total amount of lemonade in the pitcher
    result = lemonade_cups
    return result

print(solution())