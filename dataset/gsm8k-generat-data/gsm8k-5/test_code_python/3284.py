def solution():
    # Let's represent the number of loonies with L and the number of toonies with T
    # We know that L + T = 10 (Antonella has ten coins in total)
    # We also know that L + 2T - 3 = 11 (after buying the Frappuccino, she has $11 left)
    # Simplifying the above equation, we get L + 2T = 14

    # We can solve these equations using substitution or elimination
    # Here, we'll use elimination
    # Multiply the first equation by 2: 2L + 2T = 20
    # Subtract the second equation from the above: L = 6

    # Now that we know L = 6, we can solve for T
    T = 10 - L
    result = T
    return result

print(solution())