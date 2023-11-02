def solution():
    """John takes 3 naps a week. Each nap is 2 hours long. In 70 days how many hours of naps does he take?"""
    naps_per_week = 3
    nap_length = 2
    total_days = 70
    total_nap_hours = naps_per_week * nap_length * (total_days // 7)
    result = total_nap_hours
    return result

print(solution())