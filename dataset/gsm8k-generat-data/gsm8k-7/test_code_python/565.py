def solution():
    total_distance = 1000

    # Let x be the distance that Katie drives
    x = total_distance / 10  # assuming they split the distance equally

    # Michelle drives 3 times the amount that Katie drives
    michelle_distance = 3 * x

    # Tracy drives 20 miles more than twice Michelle
    tracy_distance = 2 * michelle_distance + 20

    # The total distance is the sum of all three distances
    total = tracy_distance + michelle_distance + x

    # Therefore, Michelle drives
    result = michelle_distance
    return result

print(solution())