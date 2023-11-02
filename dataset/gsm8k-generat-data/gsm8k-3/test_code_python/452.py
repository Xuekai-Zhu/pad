def solution():
    """Emily has 6 marbles. Megan gives Emily double the number she has. Emily then gives Megan back half of her new total plus 1. How many marbles does Emily have now?"""
    # Define Emily's initial number of marbles
    emily_marbles = 6

    # Megan gives Emily double the number of marbles she has
    megan_marbles = emily_marbles * 2
    emily_marbles += megan_marbles

    # Emily gives Megan back half of her new total plus 1
    emily_marbles -= (emily_marbles / 2) + 1

    # Display Emily's current number of marbles
    result = emily_marbles
    return result

print(solution())