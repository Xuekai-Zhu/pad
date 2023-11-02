def solution():
    nymph_tick_size = 1  # size in mm
    hole_punch_size = 6  # size in mm
    if nymph_tick_size < hole_punch_size:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())