def solution():
    """Jerry has a bunch of half-empty soda cans on his desk. He needs to drain all of them and put them in the recycling bin. He can carry four cans at once, and it takes him 30 seconds to drain those 4 cans. It takes him ten seconds each way to walk to the sink and recycling bin and then back to his desk. If there are 28 cans on Jerry's desk, how long does it take him to throw all of them away?"""
    cans_per_trip = 4
    time_to_drain = 30
    round_trip_time = 20
    total_cans = 28
    trips = total_cans // cans_per_trip + (total_cans % cans_per_trip > 0)
    total_time = trips * (time_to_drain + round_trip_time)
    result = total_time
    return result

print(solution())