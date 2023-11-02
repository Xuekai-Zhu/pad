def solution():
    """Harrison buys a regular croissant on Saturdays for $3.50 and an almond croissant for $5.50 on Sundays. How much does he spend on croissants in a year?"""
    regular_price = 3.5
    almond_price = 5.5
    saturday_count = 52
    sunday_count = 52
    total_cost = (regular_price * saturday_count) + (almond_price * sunday_count)
    result = total_cost
    return result

print(solution())