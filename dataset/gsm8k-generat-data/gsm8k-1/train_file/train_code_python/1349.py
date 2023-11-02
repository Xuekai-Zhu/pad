def solution():
    """John raises butterflies. He has 4 jars of 10 caterpillars each. 40% of them fail to become butterflies, but the rest become caterpillars. He sells the butterflies for $3 each. How much money does he make?"""
    total_caterpillars = 4 * 10
    successful_caterpillars = total_caterpillars * (1 - 0.4)
    butterflies = successful_caterpillars
    sale_price = 3
    total_profit = butterflies * sale_price
    result = total_profit
    return result

print(solution())