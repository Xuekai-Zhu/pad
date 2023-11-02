def solution():
    
    total_balloons = 200
    half_hour_burst = total_balloons // 5
    remaining_balloons = total_balloons - half_hour_burst
    two_hour_burst = (half_hour_burst * 2)
    remaining_balloons = remaining_balloons - two_hour_burst
    result = remaining_balloons
    return result

print(solution())