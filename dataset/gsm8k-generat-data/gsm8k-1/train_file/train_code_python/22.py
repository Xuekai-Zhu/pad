def solution():
    """Ann's favorite store was having a summer clearance. For $75 she bought 5 pairs of shorts for $7 each and 2 pairs of shoes for $10 each. She also bought 4 tops, all at the same price. How much did each top cost?"""
    shorts_price = 7
    num_shorts = 5
    shoes_price = 10
    num_shoes = 2
    total_spent = 75
    total_spent -= (shorts_price*num_shorts + shoes_price*num_shoes)
    num_tops = 4
    top_price = total_spent / num_tops
    result = top_price
    return result

print(solution())