def solution():
    num_people = 5
    num_masks = 100
    mask_life = 4  # in days

    # Calculate the number of masks used by the family every day
    masks_per_day = num_people / mask_life

    # Calculate the number of days it will take to finish the pack of masks
    num_days = num_masks / masks_per_day
    result = num_days
    return result

print(solution())