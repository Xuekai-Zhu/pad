def solution():
    """To get free delivery, Alice needs to spend a minimum of $35.00 online at her favorite grocery store. In her cart she has 1.5 pounds of chicken at $6.00 per pound, 1 pack of lettuce for $3.00, cherry tomatoes for $2.50, 4 sweet potatoes at $0.75 each, 2 heads of broccoli for $2.00 each and a pound of Brussel sprouts for $2.50. How much more does she need to spend in order to get free delivery?"""
    total_cost = (1.5 * 6) + 3 + 2.5 + (4 * 0.75) + (2 * 2) + 2.5
    if total_cost >= 35:
        result = 0
    else:
        result = 35 - total_cost
    return result

print(solution())