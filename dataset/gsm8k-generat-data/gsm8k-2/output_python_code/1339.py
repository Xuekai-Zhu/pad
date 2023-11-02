def solution():
    """William is a jockey. He can ride his horse for 6 hours a day. Over 6 days, he only used the maximum riding time twice. On two days he rode his horse for only 1.5 hours a day and half the maximum time for the next two days. How many hours did William ride his horse during those 6 days?"""
    max_time = 6
    total_days = 6
    half_max_time = max_time / 2
    full_max_count = 2
    partial_max_count = 0
    half_max_count = 2
    remaining_days = total_days - full_max_count - partial_max_count - half_max_count
    total_hours = (full_max_count * max_time) + (partial_max_count * max_time * 0.5) + (half_max_count * half_max_time) + (remaining_days * max_time)
    result = total_hours
    return result

print(solution())