def solution():
    """Luca went to a sandwich shop for lunch. The sandwich he bought was normally $8, but he had a coupon for a quarter of the price off. He then upgraded it with sliced avocado for an extra dollar. After adding a drink and a $3 salad, his total lunch bill was $12. How many dollars did Luca pay for his drink?"""
    sandwich_cost = 8
    discount = 0.25
    avocado_cost = 1
    drink_and_salad_cost = 12 - (sandwich_cost - (sandwich_cost * discount)) - avocado_cost
    drink_cost = drink_and_salad_cost - 3
    result = drink_cost
    return result

print(solution())