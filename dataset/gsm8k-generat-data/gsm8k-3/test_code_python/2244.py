def solution():
    """A farm has 5 less than 9 times the amount of hens as roosters.  If there are 75 total chickens, how many hens are there?"""
    # Define the number of roosters
    roosters = (75 - 5) / (9 + 1)

    # Define the number of hens
    hens = 9 * roosters - 5

    # Display the number of hens
    result = hens
    return result

print(solution())