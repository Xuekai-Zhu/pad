def solution():
    """A farm has 5 less than 9 times the amount of hens as roosters. If there are 75 total chickens, how many hens are there?"""
    # Define the number of roosters and hens
    roosters = None
    hens = None

    total_chickens = 75

    # Using equations to find the number of roosters and hens
    # r + h = 75
    # h = 9r - 5
    # Substituting h in terms of r into the first equation
    r = (total_chickens + 5) / 10
    h = total_chickens - r

    result = h
    return result

print(solution())