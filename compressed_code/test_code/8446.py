def solution():
    """Bob buys nose spray. He buys 10 of them for a "buy one get one free" promotion. They each cost $3. How much does he pay?"""
    num_sprays = 10
    cost_per_spray = 3
    sprays_paid_for = num_sprays / 2
    total_cost = sprays_paid_for * cost_per_spray
    result = total_cost
    return result

print(solution())