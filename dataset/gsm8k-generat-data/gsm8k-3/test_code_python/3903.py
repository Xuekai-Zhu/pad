def solution():
    """For the first hour of work, Manolo can make face-masks at the rate of one every four minutes.
    Thereafter, he can make face-masks at the rate of one every six minutes.
    How many face-masks does Manola make in a four-hour shift?"""
    
    # Calculate the number of face-masks Manolo makes in the first hour
    masks_in_hour1 = 60 // 4  # 60 minutes in an hour, he makes one every 4 minutes
    total_masks = masks_in_hour1

    # Calculate the number of face-masks Manolo makes in the remaining 3 hours
    masks_in_hour2_to_4 = (60 * 3) // 6  # he makes one every 6 minutes
    total_masks += masks_in_hour2_to_4

    # Calculate the total number of face-masks Manolo makes in the four-hour shift
    result = total_masks
    return result

print(solution())