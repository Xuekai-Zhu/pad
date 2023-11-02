def solution():
    """There are three times as many misses as hits in an MLB game. If the number of misses is 50, how many hits and misses are made in the game?"""
    # Define the number of misses
    misses = 50

    # Calculate the number of hits
    hits = misses / 3

    # Calculate the total number of hits and misses
    total = misses + hits

    # return the result
    result = (hits, misses, total)
    return result

print(solution())