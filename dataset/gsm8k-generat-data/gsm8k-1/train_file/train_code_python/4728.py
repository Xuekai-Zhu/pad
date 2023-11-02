def solution():
    """A Lamplighter monkey has long arms and can swing from branch to branch at a speed of 10 feet per second.
    But when the monkey is frightened, it will run along the branches at a speed of 15 feet per second.
    If a Lamplighter monkey runs for 5 seconds to evade a predator, then swings for another 10 seconds to add distance between itself and the predator, how far, in feet, will the monkey travel?"""
    swing_speed = 10
    run_speed = 15
    swing_time = 10
    run_time = 5
    total_distance = (swing_speed * swing_time) + (run_speed * run_time)
    result = total_distance
    return result

print(solution())