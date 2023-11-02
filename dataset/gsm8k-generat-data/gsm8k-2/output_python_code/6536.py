def solution():
    """If Alice purchased 3600 acorns for nine times the price Bob paid,
    and Bob paid $6000 for his acorns, how much money did Alice pay for each acorn?"""

    bob_price_per_acorn = 6000 / 3600
    alice_price_per_acorn = bob_price_per_acorn * 9
    result = alice_price_per_acorn
    return result

print(solution())