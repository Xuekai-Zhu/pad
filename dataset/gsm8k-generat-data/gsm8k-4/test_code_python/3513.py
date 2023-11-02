def solution():
    """James has to refuel his plane. It used to cost $200 to refill the tank. He got an extra tank to double fuel capacity. Fuel prices also went up by 20%. How much does he pay now for fuel?"""
    # Define the initial cost to refill the tank and the increase in fuel prices
    INITIAL_COST = 200
    PRICE_INCREASE = 0.2

    # Calculate the new fuel cost after the increase
    fuel_cost = INITIAL_COST * (1 + PRICE_INCREASE)

    # Double the fuel capacity by adding another tank
    fuel_cost *= 2

    # return the result
    result = fuel_cost
    return result

print(solution())