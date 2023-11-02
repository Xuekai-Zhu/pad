def solution():
    """Tamara is 3 times Kim's height less 4 inches. Tamara and Kim have a combined height of 92 inches. How many inches tall is Tamara?"""
    # Define Tamara's height as t and Kim's height as k
    # Use the equations given to form a system of equations
    # t = 3k - 4        (1)
    # t + k = 92        (2)

    # Solve for k in equation (2)
    k = 92 - t

    # Substitute k in equation (1)
    t = 3*k - 4

    # Return Tamara's height in inches
    result = t
    return result

print(solution())