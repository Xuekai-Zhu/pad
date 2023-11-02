def solution():
    outcomes = [1, 3, 2, 4, 3, 5, 3, 4, 4, 2]
    target_avg = 3
    current_avg = sum(outcomes) / len(outcomes)
    rolls_needed = target_avg * (len(outcomes) + 1) - sum(outcomes)
    result = rolls_needed
    return result

print(solution())