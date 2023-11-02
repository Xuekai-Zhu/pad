def solution():
    
    num_people = 5
    masks_per_package = 100
    mask_change_frequency = 4
    masks_used_daily = num_people / mask_change_frequency
    days_until_empty = masks_per_package / masks_used_daily
    result = days_until_empty
    return result

print(solution())