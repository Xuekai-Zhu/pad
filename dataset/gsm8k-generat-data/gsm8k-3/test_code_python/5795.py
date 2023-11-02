def solution():
    """Ariana bought a bunch of 40 flowers, 2/5 of which were roses, 10 were tulips, and the rest were carnations. How many carnations did she buy?"""
    # Calculate the number of roses
    roses = 2/5 * 40

    # Calculate the number of carnations
    carnations = 40 - roses - 10

    # Display the number of carnations
    result = carnations
    return result

print(solution())