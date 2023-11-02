def solution():
    old_shoes_speed = 6  # Candace walks 6 miles per hour in the old shoes
    hike_duration = 4  # Candace plans to hike for 4 hours
    new_shoes_speed = old_shoes_speed * 2  # The high-tech shoes will help Candace walk twice as fast
    blisters = hike_duration // 2  # Candace will get 1 blister after every 2 hours of walking

    # Calculate the speed reduction due to blisters
    speed_reduction = blisters * 2

    # Calculate the final speed in the new shoes
    final_speed = max(new_shoes_speed - speed_reduction, 0)  # Speed cannot be negative

    result = final_speed
    return result

print(solution())