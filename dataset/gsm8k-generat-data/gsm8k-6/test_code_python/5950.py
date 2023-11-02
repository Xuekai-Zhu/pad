def solution():
    # Find the number of necklaces caught by Rhonda
    rhonda_necklaces = 12 / 2  # Rhonda caught half as many necklaces as Boudreaux
    
    # Find the number of necklaces caught by Latch
    latch_necklaces = 3 * rhonda_necklaces - 4  # Latch caught four less than three times as many necklaces as Rhonda
    
    result = latch_necklaces
    return result

print(solution())