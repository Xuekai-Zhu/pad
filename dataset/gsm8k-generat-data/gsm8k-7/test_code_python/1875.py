def solution():
    rabbit_speed = 25
    cat_speed = 20
    head_start_time = 0.25 # 15 minutes = 0.25 hours
    rabbit_distance = cat_distance = 0

    # Calculate the distance travelled by cat during head start
    cat_distance = cat_speed * head_start_time

    # Calculate how long it will take for the rabbit to catch up to the cat
    time_to_catch_up = cat_distance / (rabbit_speed - cat_speed)

    result = time_to_catch_up
    return result

print(solution())