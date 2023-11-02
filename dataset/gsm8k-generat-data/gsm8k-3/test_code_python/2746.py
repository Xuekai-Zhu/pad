def solution():
    """Al is 25 pounds heavier than Ben. Ben is 16 pounds lighter than Carl. If Ed weighs 146 pounds and is 38 pounds lighter than Al, find the weight of Carl."""
    # Set up equations for the relationships between the weights
    # A = B + 25
    # B = C - 16
    # E = A - 38
    # We also know that E = 146

    # Substitute E = 146 into the equation for A
    A = 146 + 38
    # Substitute A = B + 25 into the equation for B
    B = A - 25
    # Substitute B = C - 16 into the equation for C
    C = B + 16

    # The weight of Carl is C
    result = C
    return result

print(solution())