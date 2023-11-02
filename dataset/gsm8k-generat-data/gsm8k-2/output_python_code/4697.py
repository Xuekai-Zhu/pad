def solution():
    """Andrew's father buys a package of 100 masks. Andrew lives with his 2 parents and 2 siblings. All members of Andrew's family change masks every 4 days. How many days will it take to finish the pack of masks?"""
    total_people = 5
    masks_per_day = total_people / 4
    total_masks = 100
    days_to_finish = total_masks / masks_per_day
    result = days_to_finish
    return result

print(solution())