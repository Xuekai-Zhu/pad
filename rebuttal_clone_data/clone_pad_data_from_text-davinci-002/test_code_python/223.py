def solution():
    """Andy and Bob went to the canteen to buy snacks. They spent the same amount. Andy bought a can of soda at $1 and two hamburgers at $2 each. Bob ordered two sandwiches for $3 and a can of fruit drink. How much did Bob's fruit drink cost?"""
    andy_soda_price = 1
    andy_hamburger_price = 2
    bob_sandwich_price = 3
    andy_total = andy_soda_price + (2 * andy_hamburger_price)
    bob_total = (2 * bob_sandwich_price)
    drink_price = bob_total - andy_total
    result = drink_price
    return result

print(solution())