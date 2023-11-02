def solution():
    # Calculate the number of water balloons each person filled
    balloons_max = 2 * 30 - 10  # Max filled 2 balloons/minute for 30 minutes but 10 popped
    balloons_zach = 3 * 40 - 10  # Zach filled 3 balloons/minute for 40 minutes but 10 popped

    # Calculate the total number of filled water balloons
    total_balloons = balloons_max + balloons_zach
    result = total_balloons
    return result

print(solution())