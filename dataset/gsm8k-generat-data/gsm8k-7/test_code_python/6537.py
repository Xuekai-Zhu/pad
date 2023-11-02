def solution():
    bob_price = 6000
    alice_multiple = 9
    alice_total = alice_multiple * bob_price
    num_acorns = 3600
    price_per_acorn = alice_total / num_acorns
    result = price_per_acorn
    return result

print(solution())