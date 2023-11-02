def solution():
    """Peter is raking leaves. It takes him 15 minutes to rake 3 bags of leaves. If he keeps raking at the same rate, how long will it take him to rake 8 bags?"""
    bags_per_time = 3
    time_per_bags = 15
    bags_needed = 8
    time_needed = (bags_needed / bags_per_time) * time_per_bags
    result = time_needed
    return result

print(solution())