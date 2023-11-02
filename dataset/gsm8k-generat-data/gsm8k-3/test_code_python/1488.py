def solution():
    """Bella, Monica, and Rachel are friends who like jewelry. Bella has 10 earrings, which is 25% of Monica's earrings, and Monica has twice as many earrings as Rachel. How many earrings do all of the friends have?"""
    # Let's say that Rachel has x earrings
    x = 0
    # Monica has twice as many earrings as Rachel
    m = 2 * x
    # Bella has 10 earrings, which is 25% of Monica's earrings
    b = 10
    m = b / 0.25
    # The total number of earrings is the sum of all three friends' earrings
    total = x + m + b
    result = total
    return result

print(solution())