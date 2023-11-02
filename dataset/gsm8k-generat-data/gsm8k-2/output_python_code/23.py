def solution():
    """Ann's favorite store was having a summer clearance. For $75 she bought 5 pairs of shorts for $7 each and 2 pairs of shoes for $10 each. She also bought 4 tops, all at the same price. How much did each top cost?"""
    shorts_price = 7
    shoes_price = 10
    tops_total_price = 75 - (5 * shorts_price) - (2 * shoes_price)
    tops_each_price = tops_total_price / 4
    result = tops_each_price
    return result

print(solution())