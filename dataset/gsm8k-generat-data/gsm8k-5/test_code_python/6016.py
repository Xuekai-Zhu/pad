def solution():
    total_distance = 2400
    distance_covered = 2 * 6 * 150  # 2 people, each running 6 laps of 150 meters
    remaining_distance = total_distance - distance_covered
    remaining_laps = remaining_distance / 150
    result = remaining_laps
    return result

print(solution())