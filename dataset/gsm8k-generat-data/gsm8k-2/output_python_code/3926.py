def solution():
    """Cindy can run at 3 miles per hour and walk at 1 mile per hour. If she runs for half a mile and then walks for half a mile, how many minutes will it take her to travel the full mile?"""
    run_speed = 3
    walk_speed = 1
    run_distance = 0.5
    walk_distance = 0.5
    run_time = run_distance / run_speed
    walk_time = walk_distance / walk_speed
    total_time = run_time + walk_time
    result = total_time * 60
    return result

print(solution())