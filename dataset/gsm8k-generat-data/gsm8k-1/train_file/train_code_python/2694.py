def solution():
    """Marcus spends 20 minutes giving his dog a bath and half as long blow-drying her. Then he takes her for a walk along a 3-mile trail. If Marcus walks at 6 miles per hour, how much time does he spend with his dog total?"""
    
    bath_time = 20 # in minutes
    blow_dry_time = bath_time / 2 # in minutes
    walk_distance = 3 # in miles
    walk_speed = 6 # in miles per hour
    
    # Convert all units to minutes
    walk_time = (walk_distance / walk_speed) * 60
    total_time = bath_time + blow_dry_time + walk_time
    
    return total_time

print(solution())