def solution():
    """A chocolate bar weighs 125 g. A shopkeeper has just received a 2 kilogram box of chocolate. How many bars does this represent?"""
    chocolate_weight = 125  # in grams
    box_weight = 2000  # in grams
    bar_count = box_weight // chocolate_weight
    result = bar_count
    return result

print(solution())