def solution():
    """Hayden eats 1 oz of mixed nuts as an evening snack. He buys the bulk bag of mixed nuts that cost $25.00 a bag and holds 40 oz of mixed nuts. There is currently a $5.00 coupon for this item. How much will each serving of nuts cost, in cents, after the coupon is applied?"""
    bag_cost = 25
    bag_size = 40
    coupon_amount = 5
    total_cost = bag_cost - coupon_amount
    cost_per_oz = total_cost / bag_size
    cost_per_serving = cost_per_oz * 1 * 100 # converting from dollars to cents
    result = cost_per_serving
    return result

print(solution())