def solution():
    biff_speed = 50 / 60  # convert yards per minute to yards per second
    kenneth_speed = 51 / 60  # convert yards per minute to yards per second
    race_distance = 500  # yards
    time_biff = race_distance / biff_speed  # time for Biff to complete the race
    distance_kenneth = kenneth_speed * time_biff  # distance Kenneth travels while Biff is finishing the race
    distance_past_finish = distance_kenneth - race_distance  # distance past the finish line that Kenneth travels
    result = distance_past_finish
    return result

print(solution())