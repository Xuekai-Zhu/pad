def solution():
    """Ann's favorite store was having a summer clearance. For $75 she bought 5 pairs of shorts for $7 each and 2 pairs of shoes for $10 each. She also bought 4 tops, all at the same price. How much did each top cost?"""
    cost_of_purchases = 75
    cost_of_shorts = 5 * 7
    cost_of_shoes = 2 * 10
    cost_of_tops = cost_of_purchases - cost_of_shorts - cost_of_shoes
    price_per_top = cost_of_tops / 4
    result = price_per_top

    return result

print(solution())