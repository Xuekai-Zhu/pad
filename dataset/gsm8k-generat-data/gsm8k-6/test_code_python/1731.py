def solution():
    # Calculate Ricciana's jump distance
    ricciana_jump = 4

    # Calculate Margarita's jump distance
    margarita_jump = 2 * ricciana_jump - 1

    # Calculate the total distance Margarita ran and jumped
    margarita_distance = 18 + margarita_jump

    # Calculate the total distance Ricciana ran and jumped
    ricciana_distance = 20 + ricciana_jump

    # Calculate how much farther Margarita ran and jumped than Ricciana
    difference = margarita_distance - ricciana_distance
    result = difference
    return result

print(solution())