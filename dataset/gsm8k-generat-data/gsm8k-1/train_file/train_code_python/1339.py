def solution():
    """William is a jockey. He can ride his horse for 6 hours a day. Over 6 days, he only used the maximum riding time twice. On two days he rode his horse for only 1.5 hours a day and half the maximum time for the next two days. How many hours did William ride his horse during those 6 days?"""
    max_riding_time = 6
    half_max_riding_time = max_riding_time / 2
    days_at_max = 2
    days_at_half = 2
    days_at_1_5 = 2
    total_time = (max_riding_time * days_at_max) + (half_max_riding_time * days_at_half) + (1.5 * days_at_1_5)
    result = total_time
    return result

print(solution())