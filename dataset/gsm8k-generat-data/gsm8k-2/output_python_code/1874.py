def solution():
    """Tom's rabbit can run at 25 miles per hour. His cat can run 20 miles per hour. The cat gets a 15-minute head start. In hours, how long will it take for the rabbit to catch up?"""
    rabbit_speed = 25
    cat_speed = 20
    cat_start_time = 1/4 # 15 minutes in hours
    cat_distance = cat_start_time * cat_speed
    time_to_catchup = cat_distance / (rabbit_speed - cat_speed)
    result = time_to_catchup
    return result

print(solution())