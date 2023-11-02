def solution():
    # Calculate the total distance covered by both birds in their 10 round trips
    distance_per_trip = 2 * 200  # the building materials are located 200 miles away
    total_distance = distance_per_trip * 10 * 2  # since there are 2 birds making trips
    result = total_distance
    return result

print(solution())