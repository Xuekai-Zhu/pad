def solution():
    """A cheetah can run at a top speed of 60 mph. The gazelle can run for speeds of up to 40 miles per hour. If one mile per hour is about 1.5 feet per second, then how many seconds would it take for a cheetah traveling at top speed to catch up to a fleeing gazelle also running at top speed if the two animals were initially 210 feet apart and they both traveled in the same direction?"""
    cheetah_speed_in_fps = 60 * 1.5
    gazelle_speed_in_fps = 40 * 1.5
    distance = 210
    relative_speed = cheetah_speed_in_fps - gazelle_speed_in_fps
    time = distance / relative_speed
    result = time
    return result

print(solution())