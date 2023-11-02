def solution():
    """Jeffrey owns a poultry farm with 12 hens. For every 3 hens, there is 1 rooster. Each hen has 5 chicks. How many chickens are there in all?"""
    # Calculate the number of roosters
    roosters = 12 // 3

    # Calculate the number of hens and chicks
    hens = 12
    chicks = 12 * 5

    # Calculate the total number of chickens
    total_chickens = roosters + hens + chicks

    # Display the total number of chickens
    result = total_chickens
    return result

print(solution())