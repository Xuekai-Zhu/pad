def solution():
    # Calculate the face-masks made in the first hour
    first_hour_masks = 60 / 4

    # Calculate the face-masks made in the remaining three hours
    remaining_hours_masks = (3 * 60) / 6

    # Calculate the total face-masks made in the four-hour shift
    total_masks = first_hour_masks + remaining_hours_masks
    result = total_masks
    return result

print(solution())