def solution():
    mary_distance = 630 # feet
    mary_speed = 90 # feet/minute

    ann_distance = 800 # feet
    ann_speed = 40 # feet/minute

    # Calculate the time it takes for Mary to slide down the hill
    mary_time = mary_distance / mary_speed

    # Calculate the time it takes for Ann to slide down the hill
    ann_time = ann_distance / ann_speed

    # Calculate the difference in time between Ann and Mary's trips
    time_difference = ann_time - mary_time

    result = time_difference
    return result

print(solution())