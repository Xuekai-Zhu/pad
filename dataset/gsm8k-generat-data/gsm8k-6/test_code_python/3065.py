def solution():
    original_weight = 80  # kg farmer handles per hand
    doubled_weight = original_weight * 2  # after training, he doubles this number
    specialized_weight = doubled_weight * 1.1   # he gets an extra 10% by specializing
    total_weight = specialized_weight * 2  # since he has two hands
    result = total_weight
    return result

print(solution())