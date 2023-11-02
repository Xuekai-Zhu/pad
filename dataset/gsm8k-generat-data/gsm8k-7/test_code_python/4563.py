def solution():
    num_shark_buckets = 4
    num_dolphin_buckets = num_shark_buckets / 2  # half as many buckets as sharks
    num_other_buckets = num_shark_buckets * 5  # five times as many buckets as sharks

    total_buckets = num_shark_buckets + num_dolphin_buckets + num_other_buckets

    # Calculate how many weeks the 546 buckets of fish will last
    weeks = 546 / total_buckets / 7
    result = weeks
    return result

print(solution())