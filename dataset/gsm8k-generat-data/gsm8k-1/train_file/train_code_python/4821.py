def solution():
    """James needs to get a new pair of glasses. His frames cost $200 and the lenses cost $500. Insurance will cover 80% of the cost of lenses and he has a $50 off coupon for frames. How much does everything cost?"""
    frame_cost = 200 - 50
    lens_cost = 500 * 0.2
    total_cost = frame_cost + lens_cost
    result = total_cost
    return result

print(solution())