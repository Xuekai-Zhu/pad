def solution():
    distance_per_leg = 3  # Each of the four other members runs 3 km per leg
    ralph_distance = distance_per_leg * 2  # Ralph runs twice as much as any other member, so he runs 6 km per leg
    total_distance = ralph_distance + (distance_per_leg * 4)  # Total distance is the sum of Ralph's distance and the distance covered by the other four members
    result = total_distance
    return result

print(solution())