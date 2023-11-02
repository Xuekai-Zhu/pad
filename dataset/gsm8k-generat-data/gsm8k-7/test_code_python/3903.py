def solution():
    # First hour - 15 minutes
    masks_per_minute_1 = 1/4
    masks_first_hour = masks_per_minute_1 * 60

    # Remaining 3 hours - 180 minutes
    masks_per_minute_2 = 1/6
    masks_remaining_hours = masks_per_minute_2 * 180

    # Total masks made in 4 hours
    total_masks_made = masks_first_hour + masks_remaining_hours

    result = total_masks_made
    return result

print(solution())