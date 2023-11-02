def solution():
    # Calculate the total number of balloons after inflating 4 more
    total_balloons = 2 + 4 + 4  # 2 red balloons, 4 blue balloons, and 4 more balloons

    # Calculate the probability of selecting a red balloon
    probability_red = 4 / total_balloons  # 2 red balloons + 2 new red balloons

    # Convert the probability to a percentage
    percentage_red = probability_red * 100
    result = percentage_red
    return result

print(solution())