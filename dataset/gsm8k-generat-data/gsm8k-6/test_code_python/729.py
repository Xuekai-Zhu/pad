def solution():
    # Calculate the distance John and his dog cover when they run together
    distance_together = 0.5 * (4 + 6) * 100 / 5280  # 0.5 hours (30 minutes), speed of 4 mph for John and 6 mph for the dog, and 100-pound weight of the dog
    # Calculate the distance John covers when he runs alone
    distance_alone = 0.5 * 4 / 5280  # 0.5 hours (30 minutes) and speed of 4 mph for John alone
    total_distance = distance_together + distance_alone  # Calculate the total distance covered by John in 1 hour
    result = total_distance
    return result

print(solution())