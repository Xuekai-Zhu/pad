def solution():
    """Mark bought a shirt, pants, and shoes for $340. What is the price of the pants knowing that the price of a shirt is three-quarters of the price of the pants and that the price of a shoe is ten dollars more than the price of the pants?"""
    total_price = 340
    shirt_price = 0.75 * pant_price
    shoe_price = pant_price + 10
    pant_price = (total_price - shirt_price - shoe_price) / 3
    result = pant_price
    return result

print(solution())