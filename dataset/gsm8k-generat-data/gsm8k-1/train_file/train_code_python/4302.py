def solution():
    """Jeffrey owns a poultry farm with 12 hens. For every 3 hens, there is 1 rooster. Each hen has 5 chicks. How many chickens are there in all?"""
    hens = 12
    roosters = hens // 3
    chicks = hens * 5
    total_chickens = hens + roosters + chicks
    result = total_chickens
    return result

print(solution())