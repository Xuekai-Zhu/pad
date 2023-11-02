def solution():
    """Mark bought a shirt, pants, and shoes for $340. What is the price of the pants knowing that the price of a shirt is three-quarters of the price of the pants and that the price of a shoe is ten dollars more than the price of the pants?"""
    total_cost = 340
    shirt_price_ratio = 3/4
    shoe_price_difference = 10
    
    # Let's assume the price of pants is x
    x = (total_cost - shoe_price_difference) / (1 + shirt_price_ratio + 1)
    result = x
    return result

print(solution())