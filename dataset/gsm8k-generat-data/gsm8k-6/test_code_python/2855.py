def solution():
    # Calculate the total cost of ice cream cones for 6 weeks
    cost_orange_creamsicle = 2 * 3 * 6  # Erica buys 3 orange creamsicles per week for 6 weeks at $2.00 each
    cost_ice_cream_sandwich = 1.5 * 2 * 6  # Erica buys 2 ice cream sandwiches per week for 6 weeks at $1.50 each
    cost_nutty_buddy = 3 * 2 * 6  # Erica buys 2 Nutty-Buddies per weekend for 6 weekends at $3.00 each
    total_cost = cost_orange_creamsicle + cost_ice_cream_sandwich + cost_nutty_buddy
    result = total_cost
    return result

print(solution())