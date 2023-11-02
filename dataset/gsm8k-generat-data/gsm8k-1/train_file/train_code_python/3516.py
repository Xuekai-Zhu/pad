def solution():
    """Hayden eats 1 oz of mixed nuts as an evening snack. He buys the bulk bag of mixed nuts that cost $25.00 a bag and holds 40 oz of mixed nuts. There is currently a $5.00 coupon for this item. How much will each serving of nuts cost, in cents, after the coupon is applied?"""
    total_cost = 25
    coupon = 5
    cost_after_coupon = total_cost - coupon
    total_ounces = 40
    cost_per_ounce = cost_after_coupon / total_ounces
    cost_per_serving = cost_per_ounce * 1 * 100
    result = int(cost_per_serving)
    return result

print(solution())