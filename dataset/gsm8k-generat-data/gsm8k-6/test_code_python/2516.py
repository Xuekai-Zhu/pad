def solution():
    # Calculate the total number of balloons after inflating 4 more balloons
    total_balloons = 2 + 4 + 4  # 2 red balloons, 4 blue balloons, and 4 more balloons (2 red and 2 blue)

    # Calculate the probability of selecting a red balloon
    probability_red = 4 / total_balloons  # 4 red balloons out of total_balloons
    result = probability_red * 100
    return result

print(solution())