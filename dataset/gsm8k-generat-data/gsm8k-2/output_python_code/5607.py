def solution():
    """Carl has been selling watermelons on the side of the road for $3 each. This evening he went home with $105 in profit and 18 watermelons. How many watermelons did he start out with this morning?"""
    melon_price = 3
    profit = 105
    melon_count = 18
    starting_melons = (profit + (melon_count * melon_price)) // melon_price
    result = starting_melons
    return result

print(solution())