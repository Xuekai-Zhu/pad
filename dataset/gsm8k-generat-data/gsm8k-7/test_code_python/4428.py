def solution():
    # Let x be the distance from the beginning to the first destination
    x = 0
    # The distance from the first to second destination is 2x
    distance2 = 2 * x
    # The distance from the second to third destination is 40 miles
    distance3 = 40
    # The distance from the beginning to the final destination is 2 * (x + 2x + 40) = 6x + 80
    distance4 = 6 * x + 80
    # The total distance traveled is the sum of all distances
    total_distance = x + distance2 + distance3 + distance4
    result = total_distance
    return result

print(solution())