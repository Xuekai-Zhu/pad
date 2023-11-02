def solution():
    noahs_ark_width = 75
    tunnel_lane_width = 21
    if noahs_ark_width <= tunnel_lane_width:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())