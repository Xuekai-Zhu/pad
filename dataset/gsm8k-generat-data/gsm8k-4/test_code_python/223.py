def solution():
    """Andy and Bob went to the canteen to buy snacks. They spent the same amount. Andy bought a can of soda at $1 and two hamburgers at $2 each. Bob ordered two sandwiches for $3 and a can of fruit drink. How much did Bob's fruit drink cost?"""
    # Define Andy's total cost
    andy_cost = 1 + (2 * 2)

    # Define Bob's total cost and solve for the cost of the fruit drink
    bob_cost = andy_cost
    fruit_drink_cost = bob_cost - (2 * 3)

    # Return the cost of the fruit drink
    result = fruit_drink_cost
    return result

print(solution())