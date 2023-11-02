def solution():
    """Ping pong balls sell for $.10 each. Johnny buys 10000 for a prank. He gets a 30% discount for buying in such large bulk. How much does he pay?"""
    num_balls = 10000
    price_per_ball = 0.10
    discount = 0.30
    discounted_price = price_per_ball * (1 - discount)
    total_cost = num_balls * discounted_price
    result = total_cost
    return result

print(solution())