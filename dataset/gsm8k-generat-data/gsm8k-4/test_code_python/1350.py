def solution():
    """John raises butterflies. He has 4 jars of 10 caterpillars each. 40% of them fail to become butterflies, but the rest become butterflies. He sells the butterflies for $3 each. How much money does he make?"""
    # Define the initial number of caterpillars
    initial_caterpillars = 4 * 10

    # Calculate the number of caterpillars that become butterflies
    butterflies = initial_caterpillars * (1 - 0.4)

    # Calculate the total earnings from selling the butterflies
    earnings = butterflies * 3

    result = earnings
    return result

print(solution())