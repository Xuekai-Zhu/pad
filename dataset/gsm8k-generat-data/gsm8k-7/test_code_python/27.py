def solution():
    num_initial_files = 800
    percent_deleted_round1 = 0.7
    num_second_files = 400
    fraction_deleted_round2 = 3/5

    # Calculate the number of files kept after round 1
    num_kept_round1 = num_initial_files * (1 - percent_deleted_round1)

    # Calculate the number of files kept after round 2
    num_kept_round2 = num_kept_round1 + (num_second_files * (1 - fraction_deleted_round2))

    result = num_kept_round2
    return result

print(solution())