def solution():
    sun_bear_skull_length = 262 # in mm
    black_bear_max_mouth_opening = sun_bear_skull_length / 2 # in mm
    sun_bear_size = sun_bear_skull_length / 10 # convert to cm
    black_bear_size = black_bear_max_mouth_opening / 10 # convert to cm
    if sun_bear_size < black_bear_size:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())