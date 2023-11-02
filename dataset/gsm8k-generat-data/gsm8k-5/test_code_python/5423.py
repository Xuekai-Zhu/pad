def solution():
    # Distance John skateboarded initially
    distance_skateboard = 10

    # Distance John walked to park
    distance_walk = 4

    # Total distance traveled to park
    distance_to_park = distance_skateboard + distance_walk

    # Total distance skateboarded
    distance_skate_total = 2 * distance_skateboard

    # Total distance traveled
    total_distance = distance_to_park + distance_skate_total
    result = distance_skate_total
    return result

print(solution())