def solution():
    """Jerry has a bunch of half-empty soda cans on his desk. He needs to drain all of them and put them in the recycling bin. He can carry four cans at once, and it takes him 30 seconds to drain those 4 cans. It takes him ten seconds each way to walk to the sink and recycling bin and then back to his desk. If there are 28 cans on Jerry's desk, how long does it take him to throw all of them away?"""
    cans_on_desk = 28
    cans_per_trip = 4
    drain_time = 30
    walk_time = 10
    total_trips = cans_on_desk // cans_per_trip + (1 if cans_on_desk % cans_per_trip > 0 else 0)
    total_time = total_trips * (drain_time + 2 * walk_time)
    result = total_time
    return result

print(solution())