def solution():
    """Jessica was half her mother's age when her mother died. If her mother were alive now, ten years later, she would have been 70. How old is Jessica currently?"""
    # Let Jessica's current age be x
    # Let her mother's age when she died be y
    # Then we know that x = 0.5y and y+10 = 70

    # Solving for y, we get y = 60
    y = 60

    # Substituting y in the equation x = 0.5y, we get x = 30
    x = 30

    # Jessica is currently 30 years old
    result = x
    return result

print(solution())