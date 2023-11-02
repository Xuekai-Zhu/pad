def solution():
    bob_price = 6000  # Bob paid $6000 for his acorns
    alice_price = bob_price * 9  # Alice paid 9 times the price Bob paid
    total_acorns = 3600  # Alice purchased 3600 acorns

    # Calculate how much Alice paid for each acorn
    price_per_acorn = alice_price / total_acorns
    result = price_per_acorn
    return result

print(solution())