def solution():
    num_tests = 8
    current_avg = 70
    desired_avg = 75
    max_score = 150
    base_bonus = 500
    extra_bonus = 10
    desired_total_score = (desired_avg * (num_tests + 2)) - (current_avg * num_tests)
    needed_total_score = desired_total_score - base_bonus - 600
    needed_avg_score = needed_total_score / 2
    needed_combined_score = needed_avg_score * 2
    return needed_combined_score

print(solution())