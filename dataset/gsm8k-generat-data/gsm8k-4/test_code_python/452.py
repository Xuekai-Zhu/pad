def solution():
    """Emily has 6 marbles. Megan gives Emily double the number she has. Emily then gives Megan back half of her new total plus 1. How many marbles does Emily have now?"""
    # Define the initial number of marbles Emily has
    emily_marbles = 6

    # Double the number of marbles Megan has and add it to Emily's marbles
    emily_marbles += 2 * emily_marbles

    # Calculate the number of marbles Emily gives Megan
    megan_marbles = (emily_marbles / 2) + 1

    # Subtract the number of marbles Emily gives to Megan from Emily's total
    emily_marbles -= megan_marbles

    result = emily_marbles
    return result

print(solution())