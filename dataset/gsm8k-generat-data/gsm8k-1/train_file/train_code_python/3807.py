def solution():
    """Mary just held tryouts for the high school band. 80% of the 20 flutes got in, half the 30 clarinets got in, 1/3 of the 60 trumpets got in, and 1/10th of the 20 pianists got in. How many people are in the band total?"""
    flutes_in = 0.8 * 20
    clarinets_in = 0.5 * 30
    trumpets_in = (1/3) * 60
    pianists_in = (1/10) * 20
    total_in = flutes_in + clarinets_in + trumpets_in + pianists_in
    result = total_in
    return result

print(solution())