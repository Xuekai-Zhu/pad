def solution():
    """Darry is a roofer and has to climb ladders multiple times a day. He climbs his full ladder, which has 11 steps, 10 times today. He also climbs his smaller ladder, which has 6 steps, 7 times today. He did not climb any steps otherwise. In total, how many times has Darry climbed a step today?"""
    full_ladder_steps = 11
    smaller_ladder_steps = 6
    full_ladder_climbs = 10
    smaller_ladder_climbs = 7
    total_climbs = (full_ladder_steps * full_ladder_climbs) + (smaller_ladder_steps * smaller_ladder_climbs)
    result = total_climbs
    return result

print(solution())