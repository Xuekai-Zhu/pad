def solution():
    gold_balloons = 141  # There are 141 gold balloons
    silver_balloons = 2 * gold_balloons  # There are twice as many silver balloons as gold balloons
    black_balloons = 150  # There are 150 black balloons

    # Calculate the total number of balloons
    total_balloons = gold_balloons + silver_balloons + black_balloons
    result = total_balloons
    return result

print(solution())