def solution():
    bathypelagic_zone_depth = 4000
    longest_sniper_kill_distance = 3540
    if longest_sniper_kill_distance < bathypelagic_zone_depth:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())