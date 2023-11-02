def solution():
    """Tom's rabbit can run at 25 miles per hour. His cat can run 20 miles per hour. The cat gets a 15-minute head start. In hours, how long will it take for the rabbit to catch up?"""
    rabbit_speed = 25
    cat_speed = 20
    head_start = 0.25  # 15 minutes converted to hours
    distance_traveled_by_cat = head_start * cat_speed
    time_taken_to_catch_up = distance_traveled_by_cat / (rabbit_speed - cat_speed)
    result = time_taken_to_catch_up
    return result

print(solution())