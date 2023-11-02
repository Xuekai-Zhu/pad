def solution():
    """John raises butterflies. He has 4 jars of 10 caterpillars each. 40% of them fail to become butterflies, but the rest become caterpillars. He sells the butterflies for $3 each. How much money does he make?"""
    num_caterpillars = 4 * 10
    successful_caterpillars = num_caterpillars * 0.6
    num_butterflies = successful_caterpillars / 2
    money_made = num_butterflies * 3
    result = money_made
    return result

print(solution())