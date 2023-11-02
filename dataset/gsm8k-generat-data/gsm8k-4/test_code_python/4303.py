def solution():
    """Jeffrey owns a poultry farm with 12 hens. For every 3 hens, there is 1 rooster. Each hen has 5 chicks. How many chickens are there in all?"""
    # Define the number of hens and roosters
    hens = 12
    roosters = hens // 3

    # Define the number of chicks per hen
    chicks_per_hen = 5

    # Calculate the total number of chicks
    total_chicks = hens * chicks_per_hen

    # Calculate the total number of chickens
    total_chickens = hens + roosters + total_chicks

    result = total_chickens
    return result

print(solution())