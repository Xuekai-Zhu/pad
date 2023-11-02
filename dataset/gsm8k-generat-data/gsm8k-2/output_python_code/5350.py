def solution():
    """Ellen is in charge of parking at a golf tournament. Once the main lot is full, she must direct cars to park in the overflow lot. She must transport the patrons who parked in the overflow lot up to the main lot using a golf cart. Ellen can fit 3 patrons in a golf cart. There are 12 patrons who came in cars and 27 from a bus waiting in the overflow parking lot. How many golf carts does Ellen need to transport them?"""
    car_patrons = 12
    bus_patrons = 27
    total_patrons = car_patrons + bus_patrons
    carts_needed = total_patrons // 3
    if total_patrons % 3 != 0:
        carts_needed += 1

    result = carts_needed
    return result

print(solution())