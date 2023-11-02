def solution():
    """If Alice purchased 3600 acorns for nine times the price Bob paid, and Bob paid $6000 for his acorns, how much money did Alice pay for each acorn?"""
    bob_price = 6000
    alice_price = bob_price * 9
    acorn_quantity = 3600
    price_per_acorn = alice_price / acorn_quantity
    result = price_per_acorn
    return result

print(solution())