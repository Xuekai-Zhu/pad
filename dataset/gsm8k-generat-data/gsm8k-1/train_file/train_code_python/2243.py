def solution():
    """A farm has 5 less than 9 times the amount of hens as roosters. If there are 75 total chickens, how many hens are there?"""
    total_chickens = 75
    roosters = total_chickens / 2
    hens = (9 * roosters - 5) / 2
    result = hens
    return result

print(solution())