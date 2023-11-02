def solution():
    """Andrew's father buys a package of 100 masks. Andrew lives with his 2 parents and 2 siblings. All members of Andrew's family change masks every 4 days. How many days will it take to finish the pack of masks?"""
    num_people = 5
    masks_per_package = 100
    mask_change_frequency = 4
    masks_used_daily = num_people / mask_change_frequency
    days_until_empty = masks_per_package / masks_used_daily
    result = days_until_empty
    return result

print(solution())