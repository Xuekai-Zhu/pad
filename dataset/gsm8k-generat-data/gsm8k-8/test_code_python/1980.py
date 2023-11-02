def solution():
    # Calculate the total number of balloons bought
    total_round_balloons = 5 * 20
    total_long_balloons = 4 * 30
    total_balloons = total_round_balloons + total_long_balloons

    # Subtract the burst balloons
    total_balloons -= 5

    result = total_balloons
    return result

print(solution())