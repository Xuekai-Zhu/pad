def solution():
    """For the first hour of work, Manolo can make face-masks at the rate of one every four minutes. Thereafter, he can make face-masks at the rate of one every six minutes. How many face-masks does Manola make in a four-hour shift?"""
    # Calculate the number of face-masks Manolo can make in the first hour
    masks_first_hour = 60 / 4

    # Calculate the number of face-masks Manolo can make in the remaining 3 hours
    masks_remaining_hours = (3 * 60) / 6

    # Calculate the total number of face-masks Manolo can make in a 4-hour shift
    total_masks = masks_first_hour + masks_remaining_hours

    result = total_masks
    return result

print(solution())