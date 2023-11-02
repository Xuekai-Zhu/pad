def solution():
    """At the Mystic Aquarium, sharks are fed four buckets of fish each day. The dolphins are fed half as many buckets as the
    sharks while the other sea animals are fed five times as many buckets as the sharks."""
    shark_buckets = 4
    dolphin_buckets = shark_buckets / 2
    other_buckets = shark_buckets * 5
    total_buckets_per_day = shark_buckets + dolphin_buckets + other_buckets
    total_weeks = 546 / (total_buckets_per_day * 7)
    result = total_weeks
    return result

print(solution())