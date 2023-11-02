def solution():
    """My mom went to a gardening shop. She bought a set of pots for $19 and a sack of garden soil for $26. At checkout, she used a coupon for $7 off. How much money did my mom spend at the gardening shop?"""
    pot_cost = 19
    soil_cost = 26
    coupon = 7
    total_cost = pot_cost + soil_cost - coupon
    result = total_cost
    return result

print(solution())