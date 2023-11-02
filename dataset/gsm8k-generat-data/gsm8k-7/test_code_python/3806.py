def solution():
    jellyfish_cost = x # Unknown cost of jellyfish
    eel_cost = 9 * jellyfish_cost
    
    total_cost = 200
    num_sushi_orders = 2
    
    # Set up a system of equations to solve for the cost of jellyfish
    # and eel based on the total cost and number of orders
    
    # Equation 1: jellyfish + eel = total cost
    eq1 = jellyfish_cost + eel_cost == total_cost
    
    # Equation 2: jellyfish + eel = num_sushi_orders * 2
    eq2 = jellyfish_cost + eel_cost == num_sushi_orders * 2
    
    # We can solve for jellyfish in terms of eel using either equation
    jellyfish_cost = total_cost / (1 + 9)
    eel_cost = 9 * jellyfish_cost
    
    result = eel_cost
    return result

print(solution())