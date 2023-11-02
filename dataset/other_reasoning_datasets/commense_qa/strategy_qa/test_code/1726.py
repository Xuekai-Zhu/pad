def solution():
    big_show_weight = 383
    cheetah_weight = 160
    cheetah_speed = 58
    # Convert MPH to m/s
    cheetah_speed = cheetah_speed * 0.44704
    # Find the force of the cheetah
    cheetah_force = cheetah_weight * cheetah_speed
    # Compare the force of the cheetah to the weight of Big Show
    if cheetah_force > big_show_weight:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())