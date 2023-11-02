def solution():
    """Ping pong balls sell for $.10 each. Johnny buys 10000 for a prank. He gets a 30% discount for buying in such large bulk. How much does he pay?"""
    price_per_ball = 0.10
    num_balls = 10000
    discount = 0.30
    total_price = num_balls * price_per_ball
    discounted_price = total_price - (total_price * discount)
    result = discounted_price
    return result

print(solution())