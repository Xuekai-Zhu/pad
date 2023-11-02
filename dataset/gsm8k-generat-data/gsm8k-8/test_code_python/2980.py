def solution():
    # Calculate the total number of wooden bowls sold
    total_sold = 20 * 0.5 * 10 + 20 * 0.5 * 10 + 30 * 10

    # Calculate the number of wooden bowls given as rewards
    num_rewards = total_sold // 10 * 2

    # Calculate the number of wooden bowls remaining
    num_remaining = 70 - num_rewards

    result = num_remaining
    return result

print(solution())