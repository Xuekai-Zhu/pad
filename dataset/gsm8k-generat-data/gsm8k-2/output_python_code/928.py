def solution():
    """To make a shed in his backyard, Tom needs 1000 bricks. He can buy half of the bricks for 50% off of $.50. The other Half he needs to pay full price. How many dollars does Tom spend?"""
    total_bricks = 1000
    half_bricks = total_bricks // 2
    discounted_price = 0.5
    full_price = 1.0
    half_cost = half_bricks * discounted_price * discounted_price
    other_half_cost = (total_bricks - half_bricks) * full_price
    total_cost = half_cost + other_half_cost
    result = total_cost
    return result

print(solution())