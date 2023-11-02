def solution():
    osama_height = 6.5
    tiny_house_ceiling_min = 7
    tiny_house_ceiling_max = 8
    standing_reach_avg = 8
    if osama_height + standing_reach_avg <= tiny_house_ceiling_max:
        result = "no"
    elif osama_height + standing_reach_avg >= tiny_house_ceiling_min:
        result = "yes"
    else:
        result = "unclear"
    return result

print(solution())