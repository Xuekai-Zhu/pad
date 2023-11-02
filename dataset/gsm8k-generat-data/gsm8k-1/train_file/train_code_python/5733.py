def solution():
    """Darry is a roofer and has to climb ladders multiple times a day. He climbs his full ladder, which has 11 steps, 10 times today. He also climbs his smaller ladder, which has 6 steps, 7 times today. He did not climb any steps otherwise. In total, how many times has Darry climbed a step today?"""
    steps_full_ladder = 11
    times_full_ladder = 10
    steps_small_ladder = 6
    times_small_ladder = 7
    total_steps = steps_full_ladder * times_full_ladder + steps_small_ladder * times_small_ladder
    result = total_steps
    return result

print(solution())