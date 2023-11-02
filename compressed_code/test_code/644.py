def solution():
    
    total_balloons = 200
    first_half_hour_balloons_blown = total_balloons / 5
    remaining_balloons = total_balloons - first_half_hour_balloons_blown
    second_hour_balloons_blown = 2 * first_half_hour_balloons_blown
    remaining_balloons -= second_hour_balloons_blown
    result = remaining_balloons
    return result

print(solution())