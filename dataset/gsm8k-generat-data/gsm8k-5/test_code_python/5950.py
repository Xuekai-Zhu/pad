def solution():
    boudreaux_necklaces = 12  # Boudreaux caught 12 necklaces
    rhonda_necklaces = boudreaux_necklaces * 0.5  # Rhonda caught half as many as Boudreaux
    latch_necklaces = (3 * rhonda_necklaces) - 4  # Latch caught four less than three times as many as Rhonda

    result = latch_necklaces
    return result

print(solution())