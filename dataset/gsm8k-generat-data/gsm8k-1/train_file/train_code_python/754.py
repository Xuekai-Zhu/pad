def solution():
    """Tom swims for 2 hours at a speed of 2 miles per hour. He then runs for half the time at 4 times the speed. How many miles did he cover?"""
    swim_time = 2
    swim_speed = 2
    swim_distance = swim_time * swim_speed

    run_time = swim_time / 2
    run_speed = 2 * 4
    run_distance = run_time * run_speed

    total_distance = swim_distance + run_distance
    result = total_distance
    return result

print(solution())