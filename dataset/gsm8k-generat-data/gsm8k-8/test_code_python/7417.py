def solution():
    # Calculate the number of water balloons Max fills up
    max_balloons = 2 * 30

    # Calculate the number of water balloons Zach fills up
    zach_balloons = 3 * 40

    # Calculate the total number of filled balloons (minus the ones that popped)
    total_balloons = max_balloons + zach_balloons - 10

    result = total_balloons
    return result

print(solution())