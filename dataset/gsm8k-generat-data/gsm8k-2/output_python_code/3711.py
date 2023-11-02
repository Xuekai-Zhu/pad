def solution():
    """Peter is raking leaves. It takes him 15 minutes to rake 3 bags of leaves. If he keeps raking at the same rate, how long will it take him to rake 8 bags?"""
    bags_per_time = 3
    time_per_bags = 15
    total_bags = 8
    total_time = (total_bags * time_per_bags) / bags_per_time
    result = total_time
    return result

print(solution())