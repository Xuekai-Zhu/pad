def solution():
    ricciana_run = 20
    ricciana_jump = 4
    margarita_run = 18
    margarita_jump = 2 * ricciana_jump - 1

    # Calculate the total distance that Ricciana ran and jumped
    ricciana_total = ricciana_run + ricciana_jump

    # Calculate the total distance that Margarita ran and jumped
    margarita_total = margarita_run + margarita_jump

    # Calculate the difference in distance between Margarita and Ricciana
    difference = margarita_total - ricciana_total
    result = difference
    return result

print(solution())