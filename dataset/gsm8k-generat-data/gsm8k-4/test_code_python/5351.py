def solution():
    """Ellen is in charge of parking at a golf tournament. Once the main lot is full, she must direct cars to park in the overflow lot. She must transport the patrons who parked in the overflow lot up to the main lot using a golf cart. Ellen can fit 3 patrons in a golf cart. There are 12 patrons who came in cars and 27 from a bus waiting in the overflow parking lot. How many golf carts does Ellen need to transport them?"""
    # Define the number of patrons who parked in the overflow lot
    overflow_patrons = 12 + 27

    # Calculate the number of golf carts needed to transport all the patrons
    golf_carts = (overflow_patrons // 3) + (overflow_patrons % 3 > 0)

    # Return the result
    result = golf_carts
    return result

print(solution())