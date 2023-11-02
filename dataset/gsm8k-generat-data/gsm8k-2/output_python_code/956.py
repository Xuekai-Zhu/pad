def solution():
    """A charcoal grill burns fifteen coals to ash every twenty minutes of grilling. The grill ran for long enough to burn three bags of coals. Each bag of coal contains 60 coals. How long did the grill run?"""
    coals_per_bag = 60
    total_coals = coals_per_bag * 3
    coals_burned_per_interval = 15
    intervals_needed = total_coals / coals_burned_per_interval
    time_needed = intervals_needed * 20  # 20 minutes per interval
    result = time_needed
    return result

print(solution())