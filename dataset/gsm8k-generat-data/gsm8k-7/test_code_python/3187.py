def solution():
    num_poses_per_day = 5
    num_weekdays_per_year = 260
    
    # Calculate the total number of sun salutations Summer will perform in a year
    total_poses_per_year = num_poses_per_day * num_weekdays_per_year
    
    result = total_poses_per_year
    return result

print(solution())