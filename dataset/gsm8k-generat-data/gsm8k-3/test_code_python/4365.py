def solution():
    """There are three times as many misses as hits in an MLB game. If the number of misses is 50, how many hits and misses are made in the game?"""
    # Define the ratio of misses to hits
    misses_to_hits = 3

    # Calculate the number of hits
    hits = 50 / misses_to_hits

    # Calculate the total number of hits and misses
    total = hits + 50

    # Display the number of hits and misses
    result = (hits, 50)
    return result

print(solution())