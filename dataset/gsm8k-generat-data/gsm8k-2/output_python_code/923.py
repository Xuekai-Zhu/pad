def solution():
    """There are 8 loads of laundry that need to be washed. Each load of laundry takes around 45 minutes to complete in the wash cycle and 1 hour in the dry cycle. How long, in hours, will it take to complete the entire set of laundry?"""
    wash_cycle_time = 0.75    # 45 minutes = 0.75 hours
    dry_cycle_time = 1        # 1 hour
    total_loads = 8
    total_wash_time = wash_cycle_time * total_loads
    total_dry_time = dry_cycle_time * total_loads
    total_time = total_wash_time + total_dry_time
    result = total_time
    return result

print(solution())