def solution():
    """Quentin, Skylar, and Colten have a total of 383 chickens.  Quentin has 25 more than double the chickens that Skylar has.
    Skylar has 4 less than triple the number of chickens that Colten has. How many chickens does Colten have?"""
    total_chickens = 383
    q = 2*s - 25
    s = 3*c - 4
    # Substitute s into q to get in terms of c
    q = 2*(3*c - 4) - 25
    # Solve for c
    c = (total_chickens - q - s) / 3
    result = c
    return result

print(solution())