def solution():
    original_weight = 80  # in kg
    doubled_weight = original_weight * 2
    specialized_weight = doubled_weight * 1.1  # 10% increase

    total_weight = specialized_weight + doubled_weight + original_weight
    result = total_weight
    return result

print(solution())