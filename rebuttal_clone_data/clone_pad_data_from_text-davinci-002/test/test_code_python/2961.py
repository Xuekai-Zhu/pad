def solution():
    tests_taken = 4
    total_score = 85 + 79 + 92 + 84
    average_score = total_score / tests_taken
    target_score = average_score * 5
    needed_score = target_score - total_score
    result = needed_score
    return result

print(solution())