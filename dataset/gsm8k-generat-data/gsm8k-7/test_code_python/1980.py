def solution():
    num_round_bags = 5
    round_bags_size = 20
    num_long_bags = 4
    long_bags_size = 30
    num_burst_round = 5

    # Calculate the total number of balloons Janeth bought
    total_round_balloons = num_round_bags * round_bags_size
    total_long_balloons = num_long_bags * long_bags_size
    total_balloons = total_round_balloons + total_long_balloons

    # Calculate the total number of balloons left after 5 round balloons burst
    num_balloons_left = total_balloons - num_burst_round

    result = num_balloons_left
    return result

print(solution())