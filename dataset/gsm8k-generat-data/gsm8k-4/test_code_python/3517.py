def solution():
    """Hayden eats 1 oz of mixed nuts as an evening snack. He buys the bulk bag of mixed nuts that cost $25.00 a bag and holds 40 oz of mixed nuts. There is currently a $5.00 coupon for this item. How much will each serving of nuts cost, in cents, after the coupon is applied?"""
    # Define the price of the bulk bag and the weight of the bag
    bag_price = 25.0
    bag_weight = 40.0

    # Define the coupon amount
    coupon_amount = 5.0

    # Calculate the price per oz before the coupon
    price_per_oz = bag_price / bag_weight

    # Calculate the price per oz after the coupon
    price_per_oz_after_coupon = (bag_price - coupon_amount) / bag_weight

    # Calculate the cost per serving after the coupon
    cost_per_serving = price_per_oz_after_coupon * 1.0  # 1 oz serving

    # Convert the cost per serving to cents
    cost_per_serving_cents = cost_per_serving * 100

    result = int(cost_per_serving_cents)
    return result

print(solution())