def solution():
    """Maria wants to paint a picture and needs some tools to do that. She wants to buy a set of brushes for $20 and some canvas for three times more than the brushes. The paint costs Maria $8 per liter, and she needs at least 5 liters. How much money will she earn on the painting if she will be able to sell it for $200?"""
    brush_cost = 20
    canvas_cost = 3 * brush_cost
    paint_cost = 8 * 5  # 5 liters of paint needed
    total_cost = brush_cost + canvas_cost + paint_cost
    price = 200
    profit = price - total_cost
    result = profit
    return result

print(solution())