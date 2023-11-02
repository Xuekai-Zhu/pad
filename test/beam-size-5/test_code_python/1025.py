def solution():
    
    red_balloons = 25
    green_balloons = 7
    yellow_balloons = 12
    red_burst = red_balloons * 0.4
    yellow_burst = yellow_balloons * 0.5
    red_balloons -= red_burst
    green_balloons -= green_balloons
    yellow_balloons -= yellow_balloons
    blue_balloons += 8
    clutch_balloons = blue_balloons * 0.75
    total_balloons = red_balloons + green_balloons + yellow_balloons + blue_balloons + clutch_balloons
    result = total_balloons
    return result

print(solution())