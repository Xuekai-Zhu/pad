def solution():
    """A cheetah can run at a top speed of 60 mph. The gazelle can run for speeds of up to 40 miles per hour. If one mile per hour is about 1.5 feet per second, then how many seconds would it take for a cheetah traveling at top speed to catch up to a fleeing gazelle also running at top speed if the two animals were initially 210 feet apart and they both traveled in the same direction?"""
    cheetah_speed = 60 * 1.5
    gazelle_speed = 40 * 1.5
    initial_distance = 210
    relative_speed = cheetah_speed - gazelle_speed
    time_to_catch_up = initial_distance / relative_speed
    result = time_to_catch_up
    return result

print(solution())