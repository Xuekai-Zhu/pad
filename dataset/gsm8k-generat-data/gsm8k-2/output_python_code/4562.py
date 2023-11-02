def solution():
    """At the Mystic Aquarium, sharks are fed four buckets of fish each day. The dolphins are fed half as many buckets as the sharks while the other sea animals are fed five times as many buckets as the sharks. How many weeks will 546 buckets of fish last?"""
    shark_buckets = 4
    dolphin_buckets = shark_buckets / 2
    other_buckets = shark_buckets * 5
    total_buckets = shark_buckets + dolphin_buckets + other_buckets
    weeks = 546 / total_buckets / 7
    result = weeks
    return result

print(solution())