def solution():
    # Calculate Ricciana's jump distance
    ricciana_jump = 4

    # Calculate Margarita's jump distance
    margarita_jump = 2 * ricciana_jump - 1

    # Calculate Ricciana's total distance
    ricciana_distance = 20 + ricciana_jump

    # Calculate Margarita's total distance
    margarita_distance = 18 + margarita_jump

    # Calculate the difference in distance between Margarita and Ricciana
    difference = margarita_distance - ricciana_distance

    result = difference
    return result

print(solution())