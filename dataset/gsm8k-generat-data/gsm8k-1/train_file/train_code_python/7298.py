def solution():
    """In the fall, a tree drops a tenth of its initial quantity of leaves each day over the course of four days, then abruptly drops the rest on the fifth day. If it had 340 leaves before they started to fall, how many leaves does it drop on the fifth day?"""
    initial_leaves = 340
    daily_drop = initial_leaves / 10
    total_dropped = (daily_drop * 4) + initial_leaves - daily_drop * 4
    leaves_dropped_on_fifth_day = total_dropped - initial_leaves
    result = leaves_dropped_on_fifth_day
    return result

print(solution())