def solution():
    # Calculate the total number of face-masks made by Manolo in 4 hours
    masks_first_hour = 60/4  # Manolo can make 15 face-masks in the first hour
    masks_rest_hours = 60/6 * 3  # Manolo can make 30 face-masks in the rest of the 3 hours
    total_masks = masks_first_hour + masks_rest_hours  # total number of face-masks made in 4 hours
    result = total_masks
    return result

print(solution())