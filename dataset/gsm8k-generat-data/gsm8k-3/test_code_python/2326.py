def solution():
    """Amanda’s garden contains 20 flowers and Peter’s garden contains three times as many flowers as Amanda's. If Peter gave 15 flowers to his brother, how many flowers are left in his garden?"""
    # Define the number of flowers in Amanda's garden
    amanda_flowers = 20

    # Calculate the number of flowers in Peter's garden
    peter_flowers = amanda_flowers * 3

    # Calculate the number of flowers left after Peter gave 15 to his brother
    peter_flowers_left = peter_flowers - 15

    # Display the number of flowers left in Peter's garden
    result = peter_flowers_left
    return result

print(solution())