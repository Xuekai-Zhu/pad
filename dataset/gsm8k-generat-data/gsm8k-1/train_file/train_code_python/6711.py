def solution():
    """Candace is trying to decide whether to wear her old shoes or new high-tech shoes for a hike.
    The high-tech shoes will help Candace walk twice as fast, but they're not broken in yet, so she'll get 1 blister after every 2 hours she spends walking in them.
    Each blister slows Candance down by 2 miles per hour.
    If Candace walks 6 miles per hour in the old shoes and plans to hike for 4 hours, how many miles per hour can she go in the new shoes?"""
    
    old_shoes_speed = 6
    hike_duration = 4
    new_shoes_speed = 2 * old_shoes_speed
    
    blisters_after_hours = 2
    blister_slowdown = 2
    
    total_blisters = hike_duration // blisters_after_hours
    actual_speed = new_shoes_speed - (total_blisters * blister_slowdown)
    
    result = actual_speed
    
    return result

print(solution())