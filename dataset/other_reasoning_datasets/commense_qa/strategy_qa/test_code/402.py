def solution():
    audi_top_speed = 205
    sound_barrier_speed = 770
    if audi_top_speed < sound_barrier_speed:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())