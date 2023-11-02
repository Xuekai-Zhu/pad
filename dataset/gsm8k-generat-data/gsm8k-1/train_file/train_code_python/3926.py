def solution():
    """Cindy can run at 3 miles per hour and walk at 1 mile per hour. If she runs for half a mile and then walks for half a mile, how many minutes will it take her to travel the full mile?"""
    run_speed = 3 # miles per hour
    walk_speed = 1 # mile per hour
    run_distance = 0.5 # miles
    walk_distance = 0.5 # miles
    total_distance = run_distance + walk_distance # miles
    total_time = (run_distance / run_speed) + (walk_distance / walk_speed) # hours
    total_minutes = total_time * 60 # minutes
    result = total_minutes
    return result

print(solution())