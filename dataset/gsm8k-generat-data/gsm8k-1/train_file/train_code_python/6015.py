def solution():
    """Madison and Gigi have to run a total of 2400 meters in gym class. The track is 150 meters around. If they each have run 6 laps, how many more laps do they have to run before they reach 2400 meters?"""
    total_meters = 2400
    track_distance = 150
    laps_per_person = 6
    total_laps_completed = (laps_per_person * 2)
    meters_completed = total_laps_completed * track_distance
    meters_left = total_meters - meters_completed
    laps_left = int(meters_left / track_distance)
    result = laps_left
    return result

print(solution())