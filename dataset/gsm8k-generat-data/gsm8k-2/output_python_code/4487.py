def solution():
    """Janet starts driving across a lake in a speedboat going 30 miles per hour. Her sister follows in a sailboat that has a speed of 12 miles per hour. If the lake is 60 miles wide, how long does Janet have to wait on the other side for her sister to catch up?"""
    boat_speed_diff = 30 - 12
    lake_width = 60
    time_to_cross = lake_width / 30
    time_to_catch_up = lake_width / boat_speed_diff
    waiting_time = time_to_catch_up - time_to_cross
    result = waiting_time
    return result

print(solution())