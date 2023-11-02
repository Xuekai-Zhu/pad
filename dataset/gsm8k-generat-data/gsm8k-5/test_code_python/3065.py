def solution():
    original_weight = 80  # Tom can originally lift 80 kg per hand
    doubled_weight = original_weight * 2  # After training, he can lift double the weight per hand
    specialized_weight = doubled_weight * 1.1  # After specializing, he can lift an extra 10% weight

    # Calculate the total weight Tom can hold
    total_weight = specialized_weight * 2  # Tom can hold weight in both hands
    result = total_weight
    return result

print(solution())