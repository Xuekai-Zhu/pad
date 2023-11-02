def solution():
    """A chocolate bar weighs 125 g. A shopkeeper has just received a 2 kilogram box of chocolate. How many bars does this represent?"""
    chocolate_bar_weight = 125
    total_chocolate_weight = 2000
    bars_in_box = total_chocolate_weight // chocolate_bar_weight
    result = bars_in_box
    return result

print(solution())