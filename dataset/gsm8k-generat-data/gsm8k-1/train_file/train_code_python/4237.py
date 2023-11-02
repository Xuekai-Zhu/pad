def solution():
    """Luca went to a sandwich shop for lunch. The sandwich he bought was normally $8, but he had a coupon for a quarter of the price off. He then upgraded it with sliced avocado for an extra dollar. After adding a drink and a $3 salad, his total lunch bill was $12. How many dollars did Luca pay for his drink?"""
    
    sandwich_price = 8
    coupon_discount = sandwich_price / 4
    upgraded_sandwich_price = sandwich_price - coupon_discount + 1
    drink_and_salad_price = 3 + (12 - upgraded_sandwich_price)
    drink_price = drink_and_salad_price - 3
    result = drink_price
    
    return result

print(solution())