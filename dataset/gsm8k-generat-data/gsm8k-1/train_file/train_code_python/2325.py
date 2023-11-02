def solution():
    """Amanda’s garden contains 20 flowers and Peter’s garden contains three times as many flowers as Amanda's.
    If Peter gave 15 flowers to his brother, how many flowers are left in his garden?"""
    amanda_flowers = 20
    peter_flowers = amanda_flowers * 3
    peter_flowers -= 15
    result = peter_flowers
    return result

print(solution())