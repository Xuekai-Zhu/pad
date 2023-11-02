def solution():
    """A pen and pencil have a total cost of $6. If the pen costs twice as much as the pencil, what is the cost of the pen?"""
    # Define the cost of the pen and the pencil
    pen_cost = None
    pencil_cost = None

    # Set up the system of equations
    # pen_cost + pencil_cost = 6
    # pen_cost = 2 * pencil_cost

    # Substitute the second equation into the first equation
    # 2 * pencil_cost + pencil_cost = 6
    # 3 * pencil_cost = 6
    # pencil_cost = 2

    # Use the second equation to find the cost of the pen
    pen_cost = 2 * pencil_cost

    result = pen_cost
    return result

print(solution())