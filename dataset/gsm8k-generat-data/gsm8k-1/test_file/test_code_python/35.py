def solution():
    """Dana can run at a rate of speed four times faster than she can walk, but she can skip at a rate of speed that is half as fast as she can run. If she can skip at 3 miles per hour, how many miles can she travel in six hours if she spends one-third of the time running and two-thirds of the time walking?"""
    skip_speed = 3
    run_speed = skip_speed * 2
    walk_speed = run_speed / 4
    run_time = 6 / 3
    walk_time = 6 - run_time
    run_distance = run_time * run_speed
    walk_distance = walk_time * walk_speed
    total_distance = run_distance + walk_distance
    result = total_distance
    return result

print(solution())