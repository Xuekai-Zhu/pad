def solution():
    jellyfish_cost = x  # Let the cost of jellyfish be x
    eel_cost = 9 * jellyfish_cost  # The cost of eel is nine times the cost of jellyfish

    # Set up the equation for the total cost of the two orders
    total_cost = jellyfish_cost + eel_cost

    # Solve for jellyfish_cost and then eel_cost using the total cost
    jellyfish_cost = 200 / 10  # Divide the total cost by 10 since there are two orders
    eel_cost = 9 * jellyfish_cost
    result = eel_cost
    return result

print(solution())