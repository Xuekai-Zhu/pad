def solution():
    """A banana tree has 100 bananas left after Raj cut some bananas from it. If Raj has eaten 70 bananas and has twice as many remaining in his basket, how many bananas were on the tree initially?"""
    remaining_bananas = 100
    raj_eaten = 70
    raj_remaining = 2 * (remaining_bananas - raj_eaten)
    initial_bananas = remaining_bananas + raj_eaten + raj_remaining
    result = initial_bananas
    return result

print(solution())