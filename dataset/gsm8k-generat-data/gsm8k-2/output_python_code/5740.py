def solution():
    """Keesha wants to get her hair and nails done for prom. Hair updos cost $50 and manicures cost $30. How much will these two services cost her with a 20% tip for each beautician?"""
    hair_cost = 50
    nail_cost = 30
    tip_rate = 0.2
    hair_tip = hair_cost * tip_rate
    nail_tip = nail_cost * tip_rate
    total_cost = hair_cost + nail_cost + hair_tip + nail_tip
    result = total_cost
    return result

print(solution())