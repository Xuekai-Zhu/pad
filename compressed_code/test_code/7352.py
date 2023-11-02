def solution():
    
    round_bags = 5
    round_balloons_per_bag = 20
    long_bags = 4
    long_balloons_per_bag = 30
    total_round_balloons = round_bags * round_balloons_per_bag
    total_long_balloons = long_bags * long_balloons_per_bag
    total_balloons = total_round_balloons + total_long_balloons
    balloons_burst = 5
    balloons_left = total_balloons - balloons_burst
    result = balloons_left
    return result

print(solution())