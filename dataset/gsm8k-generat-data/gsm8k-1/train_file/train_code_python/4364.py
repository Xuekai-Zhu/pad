def solution():
    """There are three times as many misses as hits in an MLB game. If the number of misses is 50, how many hits and misses are made in the game?"""
    misses = 50
    hits = misses / 3
    total_hits_misses = misses + hits
    result = (hits, misses, total_hits_misses)
    return result

print(solution())