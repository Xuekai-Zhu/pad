def solution():
    """Amanda’s garden contains 20 flowers and Peter’s garden contains three times as many flowers as Amanda's. If Peter gave 15 flowers to his brother, how many flowers are left in his garden?"""
    amandas_flowers = 20
    peters_flowers = 3 * amandas_flowers
    peters_flowers -= 15
    result = peters_flowers
    return result

print(solution())