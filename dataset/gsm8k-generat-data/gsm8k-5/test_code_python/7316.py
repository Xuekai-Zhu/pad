def solution():
    jars = 4
    cucumbers = 10
    vinegar = 100

    # Calculate how many pickles can be made
    pickles = min(cucumbers * 6, jars * 12)

    # Calculate how much vinegar is needed for the pickles
    vinegar_needed = pickles / 12 * 10

    # Calculate how much vinegar is left
    vinegar_left = vinegar - vinegar_needed
    result = vinegar_left
    return result

print(solution())