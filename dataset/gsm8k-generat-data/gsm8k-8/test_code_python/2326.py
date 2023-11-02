def solution():
    # Define the number of flowers in Amanda's garden
    amanda_flowers = 20

    # Calculate the number of flowers in Peter's garden
    peter_flowers = 3 * amanda_flowers

    # Calculate the number of flowers left in Peter's garden after giving some to his brother
    peter_flowers_left = peter_flowers - 15

    result = peter_flowers_left
    return result

print(solution())