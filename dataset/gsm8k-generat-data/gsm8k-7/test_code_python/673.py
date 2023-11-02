def solution():
    ball_price = 0.10
    num_balls = 10000
    discount = 0.30  # 30% discount

    # Calculate the total price for all balls without discount
    total_price = ball_price * num_balls

    # Calculate the discount amount
    discount_amount = total_price * discount

    # Calculate the total price after discount
    total_price_after_discount = total_price - discount_amount
    result = total_price_after_discount
    return result

print(solution())