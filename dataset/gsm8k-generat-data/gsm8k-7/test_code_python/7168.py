def solution():
    total_attempts = 60
    missed_fraction = 1/4
    missed_total = missed_fraction * total_attempts
    missed_wide_right_fraction = 0.2
    missed_wide_right = missed_wide_right_fraction * missed_total
    result = missed_wide_right
    return result

print(solution())