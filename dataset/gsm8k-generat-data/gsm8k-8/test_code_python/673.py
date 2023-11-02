def solution():
    # Define the price and quantity of the ping pong balls
    price_per_ball = 0.10
    quantity = 10000

    # Calculate the discounted price
    discount_percent = 30
    discount_amount = discount_percent / 100 * price_per_ball * quantity
    discounted_price = price_per_ball * quantity - discount_amount

    result = discounted_price
    return result

print(solution())