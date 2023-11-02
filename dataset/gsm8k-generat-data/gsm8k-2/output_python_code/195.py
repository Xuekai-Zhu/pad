def solution():
    """Mary bought 5 boxes of drinks at $6 each box and 10 boxes of pizzas at $14 each box for her pizza party. She paid $200 for all the items. How much change did she get back?"""
    drink_price = 6
    pizza_price = 14
    total_boxes = 5 + 10
    total_cost = (5 * drink_price) + (10 * pizza_price)
    change = 200 - total_cost
    result = change
    return result

print(solution())