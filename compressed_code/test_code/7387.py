def solution():
    
    initial_red_balloons = 20
    initial_green_balloons = 15
    red_burst = 3
    green_burst = 2
    remaining_red = initial_red_balloons - red_burst
    remaining_green = initial_green_balloons - green_burst
    total_balloons = remaining_red + remaining_green
    result = total_balloons
    return result

print(solution())