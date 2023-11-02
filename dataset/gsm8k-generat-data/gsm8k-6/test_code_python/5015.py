def solution():
    # Let x = the time it takes for Jack to cycle from the store to Peter's house
    # Then 2x = the time it takes for Jack to cycle from his home to the store
    # Let s = Jack's speed in miles per hour

    # Distance from home to store = s * 2x
    # Distance from store to Peter's house = s * x
    # Total distance cycled = s * 3x + 50 (round-trip from store to Peter's)

    # since it takes twice as long for Jack to go from home to store as from store to Peter's:
    2*x = 4*x / 2
    x = 2   # hours

    # Total distance cycled
    total_distance = 3*s*x + 50
    result = total_distance
    return result

print(solution())