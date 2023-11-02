def solution():
    """Marilyn's first record sold 10 times as many copies as Harald's. If they sold 88,000 copies combined, how many copies did Harald sell?"""
    total_copies = 88000
    ratio = 1 / 11
    harald_copies = total_copies / (1 + ratio)
    result = harald_copies
    return result

print(solution())