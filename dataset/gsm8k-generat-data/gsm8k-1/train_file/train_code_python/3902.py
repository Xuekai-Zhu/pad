def solution():
    """For the first hour of work, Manolo can make face-masks at the rate of one every four minutes. Thereafter, he can make face-masks at the rate of one every six minutes. How many face-masks does Manola make in a four-hour shift?"""
    masks_per_hour_1 = 15  # 60/4
    masks_per_hour_2 = 10  # 60/6
    total_masks = (masks_per_hour_1 * 1) + (masks_per_hour_2 * 3)
    result = total_masks * 4
    return result

print(solution())