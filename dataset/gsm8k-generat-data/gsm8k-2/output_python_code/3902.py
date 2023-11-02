def solution():
    """For the first hour of work, Manolo can make face-masks at the rate of one every four minutes. Thereafter, he can make face-masks at the rate of one every six minutes. How many face-masks does Manola make in a four-hour shift?"""
    first_hour_rate = 1 / 4  # one mask every 4 minutes
    remaining_hours_rate = 1 / 6  # one mask every 6 minutes
    total_time = 240  # 4 hours in minutes
    first_hour_made = int(total_time / 60 * first_hour_rate)  # masks made in the first hour
    remaining_hours_made = int((total_time - 60) / 60 * remaining_hours_rate)  # masks made in remaining hours
    total_masks_made = first_hour_made + remaining_hours_made
    result = total_masks_made
    return result

print(solution())