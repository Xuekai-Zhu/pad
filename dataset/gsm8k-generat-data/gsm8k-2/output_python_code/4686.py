def solution():
    """Delaney has to catch a bus that leaves at 8:00. a.m to school every day. He always takes 30 minutes to reach the pick-up point from his home. One day he woke up late and left his home at 7:50. How much time did he miss the bus by when he reached the pick-up point?"""
    time_to_reach_pickup_point = 30
    bus_departure_time = 8*60
    delaney_departure_time = 7*60+50
    miss_time = bus_departure_time-(delaney_departure_time+time_to_reach_pickup_point)
    result = miss_time
    return result

print(solution())