def solution():
    """Delaney has to catch a bus that leaves at 8:00. a.m to school every day. He always takes 30 minutes to reach the pick-up point from his home. One day he woke up late and left his home at 7:50. How much time did he miss the bus by when he reached the pick-up point?"""
    bus_time = 8 * 60  # convert time to minutes, bus leaves at 8:00 a.m
    travel_time = 30
    late_start = 7 * 60 + 50  # convert time to minutes, Delaney left home at 7:50 a.m
    missed_time = bus_time - (late_start + travel_time)
    result = missed_time
    return result

print(solution())