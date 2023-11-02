def solution():
    red_balloons = 20
    green_balloons = 15
    red_balloons_burst = 3
    green_balloons_burst = 2
    red_balloons_left = red_balloons - red_balloons_burst
    green_balloons_left = green_balloons - green_balloons_burst
    total_balloons_left = red_balloons_left + green_balloons_left
    result = total_balloons_left
    
    return result

print(solution())