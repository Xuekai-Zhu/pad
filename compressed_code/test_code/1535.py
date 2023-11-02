def solution():
    
    round_bags = 5
    round_per_bag = 20
    long_bags = 4
    long_per_bag = 30
    total_round = round_bags * round_per_bag - 5
    total_long = long_bags * long_per_bag
    total_balloons = total_round + total_long
    result = total_balloons
    return result

print(solution())