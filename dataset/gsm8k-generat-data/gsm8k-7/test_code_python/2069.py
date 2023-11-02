def solution():
    num_shoes = 80
    donation_percent = 0.3  # 30% donation
    num_donated = num_shoes * donation_percent
    num_kept = num_shoes - num_donated

    # Add 6 new pairs
    num_kept += 6

    result = num_kept
    return result

print(solution())