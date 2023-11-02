def solution():
    """Ellen is in charge of parking at a golf tournament. Once the main lot is full, she must direct cars to park in the overflow lot. She must transport the patrons who parked in the overflow lot up to the main lot using a golf cart. Ellen can fit 3 patrons in a golf cart. There are 12 patrons who came in cars and 27 from a bus waiting in the overflow parking lot. How many golf carts does Ellen need to transport them?"""
    # Define the number of patrons and the capacity of a golf cart
    CAR_PATRONS = 12
    BUS_PATRONS = 27
    CART_CAPACITY = 3

    # Calculate the total number of patrons
    total_patrons = CAR_PATRONS + BUS_PATRONS

    # Calculate the number of golf carts needed
    carts_needed = (total_patrons // CART_CAPACITY) + (1 if total_patrons % CART_CAPACITY != 0 else 0)

    # Display the number of golf carts needed
    result = carts_needed
    return result

print(solution())