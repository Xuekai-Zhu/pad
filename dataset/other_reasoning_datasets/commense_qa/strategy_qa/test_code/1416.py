def solution():
    daytona_500_distance = 500
    hoverboard_speed = 6 # assume using the slower speed of 6 mph
    hoverboard_time = daytona_500_distance / hoverboard_speed
    e6000_min_cure_time = 24
    e6000_max_cure_time = 72
    if e6000_max_cure_time < hoverboard_time:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())