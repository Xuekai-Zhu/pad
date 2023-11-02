def solution():
    """Carla's teacher tells her that she needs to collect 30 leaves and 20 bugs for a project that's due in 10 days. How many items does Carla need to collect each day if she always wants to collect the same daily amount?"""
    total_leaves = 30
    total_bugs = 20
    total_days = 10
    daily_items = (total_leaves + total_bugs) / total_days
    result = daily_items
    return result

print(solution())