def solution():
    # Calculate the total cost of 10000 ping pong balls with a 30% discount
    cost_per_ball = 0.10
    total_balls = 10000
    discount = 0.30
    cost_before_discount = cost_per_ball * total_balls
    cost_after_discount = cost_before_discount * (1 - discount)
    result = cost_after_discount
    return result

print(solution())