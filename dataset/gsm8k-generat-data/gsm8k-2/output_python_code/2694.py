def solution():
    """Marcus spends 20 minutes giving his dog a bath and half as long blow-drying her. Then he takes her for a walk along a 3-mile trail. If Marcus walks at 6 miles per hour, how much time does he spend with his dog total?"""
    bath_time = 20
    dry_time = bath_time / 2
    walk_distance = 3
    walk_speed = 6
    walk_time = walk_distance / walk_speed
    total_time = bath_time + dry_time + walk_time * 60
    result = total_time
    return result

print(solution())