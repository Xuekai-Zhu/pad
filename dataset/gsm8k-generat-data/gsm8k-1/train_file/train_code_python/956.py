def solution():
    """A charcoal grill burns fifteen coals to ash every twenty minutes of grilling. The grill ran for long enough to burn three bags of coals. Each bag of coal contains 60 coals. How long did the grill run?"""
    coals_per_cycle = 15
    time_per_cycle = 20
    coals_per_bag = 60
    total_coals = coals_per_bag * 3
    cycles = total_coals / coals_per_cycle
    total_time = cycles * time_per_cycle
    result = total_time
    return result

print(solution())