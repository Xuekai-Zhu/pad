def solution():
    # Calculate distance covered during each leg of the journey
    distance_flat = 20 * 4.5
    distance_incline = 12 * 2.5
    distance_coast = 24 * 1.5

    # Calculate total distance covered before puncture
    total_distance = distance_flat + distance_incline + distance_coast

    # Calculate distance left to travel after puncture
    distance_left = 164 - total_distance

    result = distance_left
    return result

print(solution())