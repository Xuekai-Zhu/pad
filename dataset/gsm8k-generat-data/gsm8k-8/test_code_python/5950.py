def solution():
    # Calculate the number of necklaces caught by Rhonda
    rhonda_catches = 12 / 2

    # Calculate the number of necklaces caught by Latch
    latch_catches = 3 * rhonda_catches - 4

    result = latch_catches
    return result

print(solution())