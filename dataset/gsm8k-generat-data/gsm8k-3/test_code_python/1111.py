def solution():
    """Barbara asked the butcher for 4 1/2 pound steaks that cost $15.00/pound. She also asked for a pound and half of chicken breasts that were $8.00 a pound. How much did she spend at the butchers?"""
    # Define the cost of the steaks per pound and the amount of steaks purchased
    STEAK_PRICE = 15
    STEAK_WEIGHT = 4.5

    # Define the cost of the chicken breasts per pound and the amount purchased
    CHICKEN_PRICE = 8
    CHICKEN_WEIGHT = 1.5

    # Calculate the total cost of the steaks
    steak_cost = STEAK_PRICE * STEAK_WEIGHT

    # Calculate the total cost of the chicken breasts
    chicken_cost = CHICKEN_PRICE * CHICKEN_WEIGHT

    # Calculate the total cost of the purchase
    total_cost = steak_cost + chicken_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())