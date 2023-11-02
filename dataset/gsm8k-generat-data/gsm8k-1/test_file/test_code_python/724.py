def solution():
    """Candy has 15 light blue spools of thread, 45 dark blue spools of thread, 40 light green spools of thread, and 50 dark green spools of thread. What percent of her spools are blue?"""
    blue_spools = 15 + 45
    total_spools = blue_spools + 40 + 50
    percent_blue = (blue_spools / total_spools) * 100
    result = percent_blue
    return result

print(solution())