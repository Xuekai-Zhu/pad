def solution():
    """There's a sale at your favorite "Any item $10" retailer. If you buy 1 shirt you pay $10. If you buy 2, you get the second one at a 50% discount. If you buy 3, you get the third one at a 60% discount. How much money did you save if you bought 3 shirts?"""
    shirt_price = 10
    discount_2_shirts = 0.5
    discount_3_shirts = 0.6
    total_cost_1 = shirt_price * 1
    total_cost_2 = shirt_price + shirt_price * discount_2_shirts
    total_cost_3 = shirt_price + shirt_price * discount_2_shirts + shirt_price * discount_3_shirts
    total_savings = (total_cost_1 + total_cost_2 + total_cost_3) - (10 * 3)
    result = total_savings
    return result

print(solution())