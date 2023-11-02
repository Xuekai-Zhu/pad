def solution():
    # John's starting weights
    clean_jerk_start = 80
    snatch_start = 50

    # John's new weights
    clean_jerk_new = clean_jerk_start * 2
    snatch_new = snatch_start * 1.8

    # John's new total lifting capacity
    total_new = clean_jerk_new + snatch_new
    result = total_new
    return result

print(solution())