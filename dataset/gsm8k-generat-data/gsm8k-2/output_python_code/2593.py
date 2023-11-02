def solution():
    """John plays paintball 3 times a month. Each time he plays he buys 3 boxes of paintballs. They cost $25 per box. How much does he spend a month on paintballs?"""
    times_per_month = 3
    boxes_per_time = 3
    box_price = 25
    total_spent = times_per_month * boxes_per_time * box_price
    result = total_spent
    return result

print(solution())