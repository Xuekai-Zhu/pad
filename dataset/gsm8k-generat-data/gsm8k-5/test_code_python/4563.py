def solution():
    shark_buckets_per_day = 4
    dolphin_buckets_per_day = shark_buckets_per_day / 2
    other_buckets_per_day = shark_buckets_per_day * 5

    total_buckets_per_day = shark_buckets_per_day + dolphin_buckets_per_day + other_buckets_per_day

    # Calculate the number of weeks 546 buckets will last
    buckets_needed_for_1_week = total_buckets_per_day * 7
    weeks = 546 / buckets_needed_for_1_week
    result = weeks
    return result

print(solution())