def solution():
    """Ellen is in charge of parking at a golf tournament. Once the main lot is full, she must direct cars to park in the overflow lot.
    She must transport the patrons who parked in the overflow lot up to the main lot using a golf cart. Ellen can fit 3 patrons in a golf cart.
    There are 12 patrons who came in cars and 27 from a bus waiting in the overflow parking lot. How many golf carts does Ellen need to transport them?"""
    total_patrons = 12 + 27
    carts_needed = total_patrons // 3 + (1 if total_patrons % 3 != 0 else 0)
    result = carts_needed
    return result

print(solution())