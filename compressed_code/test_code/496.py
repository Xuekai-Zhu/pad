def solution():
    
    price_per_ball = 0.10
    num_balls = 10000
    discount = 0.30
    total_price = num_balls * price_per_ball
    discounted_price = total_price - (total_price * discount)
    result = discounted_price
    return result

print(solution())