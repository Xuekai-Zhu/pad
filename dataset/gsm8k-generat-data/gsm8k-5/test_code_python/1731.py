def solution():
    # Distance Ricciana jumped
    ricciana_jump = 4

    # Distance Margarita jumped
    margarita_jump = 2 * ricciana_jump - 1

    # Total distance Ricciana ran and jumped
    ricciana_total = 20 + ricciana_jump

    # Total distance Margarita ran and jumped
    margarita_total = 18 + margarita_jump

    # Calculate how much farther Margarita ran and jumped compared to Ricciana
    difference = margarita_total - ricciana_total
    result = difference
    return result

print(solution())