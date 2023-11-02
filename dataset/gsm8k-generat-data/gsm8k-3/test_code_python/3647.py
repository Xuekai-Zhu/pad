def solution():
    """Carla's order at Mcdonald's costs $7.50, but she has a coupon for $2.50. If she gets an additional 20% discount for being a senior citizen, how much does she pay for her order in dollars total?"""
    # Define the original cost of the meal and the coupon amount
    original_cost = 7.50
    coupon_amount = 2.50

    # Calculate the discounted cost after using the coupon
    discounted_cost = original_cost - coupon_amount

    # Calculate the additional discount for being a senior citizen
    senior_discount = 0.20 * discounted_cost

    # Calculate the final cost after all discounts
    final_cost = discounted_cost - senior_discount

    # Display the final cost
    result = final_cost
    return result

print(solution())