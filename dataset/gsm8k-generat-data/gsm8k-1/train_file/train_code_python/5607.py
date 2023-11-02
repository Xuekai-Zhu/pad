def solution():
    """Carl has been selling watermelons on the side of the road for $3 each. This evening he went home with $105 in profit and 18 watermelons. How many watermelons did he start out with this morning?"""
    price_per_watermelon = 3
    profit = 105
    total_watermelons = 18
    starting_watermelons = (profit + (price_per_watermelon * total_watermelons)) / price_per_watermelon
    result = starting_watermelons
    return result

print(solution())