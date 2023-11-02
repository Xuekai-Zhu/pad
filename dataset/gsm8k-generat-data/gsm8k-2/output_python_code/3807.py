def solution():
    """Mary just held tryouts for the high school band. 80% of the 20 flutes got in, half the 30 clarinets got in, 1/3 of the 60 trumpets got in, and 1/10th of the 20 pianists got in. How many people are in the band total?"""
    flutes = round(0.8 * 20)
    clarinets = round(0.5 * 30)
    trumpets = round(1/3 * 60)
    pianists = round(0.1 * 20)
    total = flutes + clarinets + trumpets + pianists
    result = total
    return result

print(solution())