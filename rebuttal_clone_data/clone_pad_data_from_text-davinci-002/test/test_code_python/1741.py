def solution():
    green_mms = 20
    red_mms = 20
    yellow_mms = 14
    total_mms = green_mms + red_mms + yellow_mms
    eaten_green_mms = 12
    remaining_green_mms = green_mms - eaten_green_mms
    eaten_red_mms = red_mms / 2
    remaining_red_mms = red_mms - eaten_red_mms
    total_remaining_mms = remaining_green_mms + remaining_red_mms + yellow_mms
    percentage_chance_green = (remaining_green_mms / total_remaining_mms) * 100
    result = percentage_chance_green
    
    return result

print(solution())