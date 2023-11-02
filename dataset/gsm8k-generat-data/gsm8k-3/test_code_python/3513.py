def solution():
    """James has to refuel his plane.  It used to cost $200 to refill the tank.  He got an extra tank to double fuel capacity.  Fuel prices also went up by 20%.  How much does he pay now for fuel?"""
    # Define the original cost and the percentage increase in fuel prices
    original_cost = 200
    percent_increase = 0.2

    # Calculate the new cost of fuel
    new_capacity = 2 * original_capacity
    new_cost = (1 + percent_increase) * original_cost * new_capacity / original_capacity

    # Display the new cost of fuel
    result = new_cost
    return result

print(solution())