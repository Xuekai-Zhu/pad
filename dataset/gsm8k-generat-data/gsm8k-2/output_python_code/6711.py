def solution():
    """Candace is trying to decide whether to wear her old shoes or new high-tech shoes for a hike. The high-tech shoes will help Candace walk twice as fast, but they're not broken in yet, so she'll get 1 blister after every 2 hours she spends walking in them. Each blister slows Candace down by 2 miles per hour. If Candace walks 6 miles per hour in the old shoes and plans to hike for 4 hours, how many miles per hour can she go in the new shoes?"""
    old_speed = 6
    hike_duration = 4
    new_speed = 2 * old_speed

    blisters = hike_duration // 2
    speed_reduction = blisters * 2

    final_speed = new_speed - speed_reduction
    result = final_speed
    return result

print(solution())