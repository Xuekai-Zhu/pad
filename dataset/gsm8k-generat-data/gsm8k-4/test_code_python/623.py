def solution():
    """Abigail is trying a new recipe for a cold drink. It uses 1/4 of a cup of iced tea and 1 and 1/4 of a cup of lemonade to make one drink. If she fills a pitcher with 18 total cups of this drink, how many cups of lemonade are in the pitcher?"""
    # Define the proportions of iced tea and lemonade in one drink
    iced_tea_per_drink = 1/4
    lemonade_per_drink = 1 + 1/4

    # Calculate the total number of drinks in the pitcher
    total_drinks = 18 / lemonade_per_drink

    # Calculate the total amount of lemonade in the pitcher
    total_lemonade = total_drinks * lemonade_per_drink

    # return the result
    result = total_lemonade
    return result

print(solution())