def solution():
    """Maddie went to a beauty store and bought some beauty products. She bought 3 different makeup palettes which cost $15 each, 4 lipsticks which cost $2.50, and 3 boxes of hair color which cost $4 each. How much did Maddie pay in total?"""
    makeup_price = 15
    lipstick_price = 2.5
    hair_color_price = 4
    total_makeup_price = 3 * makeup_price
    total_lipstick_price = 4 * lipstick_price
    total_hair_color_price = 3 * hair_color_price
    total_price = total_makeup_price + total_lipstick_price + total_hair_color_price
    result = total_price
    return result

print(solution())