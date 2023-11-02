def solution():
    """Ping pong balls sell for $.10 each. Johnny buys 10000 for a prank. He gets a 30% discount for buying in such large bulk. How much does he pay?"""
    # Define the price of each ping pong ball and the number of balls purchased
    BALL_PRICE = 0.10
    BALLS_PURCHASED = 10000

    # Calculate the discount amount and the discounted price per ball
    DISCOUNT = 0.30
    DISCOUNT_AMOUNT = BALL_PRICE * BALLS_PURCHASED * DISCOUNT
    DISCOUNTED_PRICE = BALL_PRICE - DISCOUNT_AMOUNT

    # Calculate the total amount paid for the balls
    TOTAL_PRICE = DISCOUNTED_PRICE * BALLS_PURCHASED

    # Return the result
    result = TOTAL_PRICE
    return result

print(solution())