def solution():
    current_sum = 25  # Ronald has already rolled 9 times and has a sum of 25
    current_avg = current_sum / 9  # Calculate the current average

    # Ronald needs to roll x on the next roll to achieve an average of 3
    # So, (current_sum + x) / (9 + 1) = 3
    # Therefore, x = (3 * (9 + 1)) - current_sum
    next_roll = (3 * (9 + 1)) - current_sum
    result = next_roll
    return result

print(solution())