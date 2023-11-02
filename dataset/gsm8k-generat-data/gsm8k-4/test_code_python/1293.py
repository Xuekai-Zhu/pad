def solution():
    """Jimmy and Irene go shopping for clothes on a Tuesday, where senior citizens get a 10% discount on their purchases. Jimmy picks out 3 shorts from the $15 rack. Irene grabs 5 shirts from the $17 rack. How much money do they give to the cashier?"""
    # Define the prices of the shorts and shirts
    shorts_price = 15
    shirts_price = 17

    # Calculate the total cost of Jimmy's shorts and Irene's shirts before the discount
    jimmy_cost = 3 * shorts_price
    irene_cost = 5 * shirts_price
    total_cost = jimmy_cost + irene_cost

    # Calculate the discount amount for seniors
    senior_discount = total_cost * 0.1

    # Calculate the total cost after the discount
    total_cost_discounted = total_cost - senior_discount

    # Return the result
    result = total_cost_discounted
    return result

print(solution())