def solution():
    
    red_balloons = 25
    green_balloons = 7
    yellow_balloons = 12
    red_burst = red_balloons * 0.4
    green_burst = green_balloons * 0.5
    yellow_burst = yellow_balloons * 0.5
    remaining_balloons = red_balloons + green_balloons + yellow_balloons - red_burst - green_burst - yellow_burst
    blue_balloons = 8
    clutch_added = remaining_balloons * 0.75
    total_clutch_added = clutch_added + remaining_balloons
    result = total_clutch_added
    return result

print(solution())