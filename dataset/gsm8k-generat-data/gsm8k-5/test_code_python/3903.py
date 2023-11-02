def solution():
    # Calculate the number of face-masks Manolo can make in the first hour
    masks_first_hour = 60 / 4  # Manolo can make 15 masks in the first hour

    # Calculate the number of face-masks Manolo can make in the remaining three hours
    masks_remaining_time = 3 * 60 / 6  # Manolo can make 30 masks in the remaining three hours

    # Calculate the total number of face-masks Manolo can make in the four-hour shift
    total_masks = masks_first_hour + masks_remaining_time
    result = total_masks
    return result

print(solution())