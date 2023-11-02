def solution():
    """Madison and Gigi have to run a total of 2400 meters in gym class. The track is 150 meters around. If they each have run 6 laps, how many more laps do they have to run before they reach 2400 meters?"""
    total_distance = 2400
    lap_distance = 150 * 6
    remaining_distance = total_distance - lap_distance
    remaining_laps = remaining_distance / 150
    result = remaining_laps
    return result

print(solution())