def solution():
    """Amanda’s garden contains 20 flowers and Peter’s garden contains three times as many flowers as Amanda's. If Peter gave 15 flowers to his brother, how many flowers are left in his garden?"""
    # Define the initial number of flowers in Amanda's garden
    amanda_flowers = 20

    # Calculate the number of flowers in Peter's garden
    peter_flowers = amanda_flowers * 3

    # Subtract the number of flowers Peter gave to his brother
    peter_flowers -= 15

    result = peter_flowers
    return result

print(solution())