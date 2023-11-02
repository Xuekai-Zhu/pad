def solution():
    """Abigail is trying a new recipe for a cold drink. It uses 1/4 of a cup of iced tea and 1 and 1/4 of a cup of lemonade to make one drink. If she fills a pitcher with 18 total cups of this drink, how many cups of lemonade are in the pitcher?"""
    iced_tea_per_drink = 0.25
    lemonade_per_drink = 1.25
    total_cups_per_drink = iced_tea_per_drink + lemonade_per_drink
    total_drinks = 18 / total_cups_per_drink
    cups_of_lemonade = total_drinks * lemonade_per_drink
    result = cups_of_lemonade
    return result

print(solution())