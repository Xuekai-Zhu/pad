def solution():
    """Ariana bought a bunch of 40 flowers, 2/5 of which were roses, 10 were tulips, and the rest were carnations. How many carnations did she buy?"""
    total_flowers = 40
    roses = (2/5) * total_flowers
    tulips = 10
    carnations = total_flowers - roses - tulips
    result = carnations
    return result

print(solution())