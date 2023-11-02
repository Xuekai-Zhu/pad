def solution():
    """Keesha wants to get her hair and nails done for prom. Hair updos cost $50 and manicures cost $30. How much will these two services cost her with a 20% tip for each beautician?"""
    hair_cost = 50
    manicure_cost = 30
    tip_percent = 20
    hair_tip = hair_cost * (tip_percent / 100)
    manicure_tip = manicure_cost * (tip_percent / 100)
    total_cost = hair_cost + manicure_cost + hair_tip + manicure_tip
    result = total_cost
    return result

print(solution())