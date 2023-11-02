def solution():
    # Calculate the total time John plays
    total_time = 2 * 12 # 2 periods of 12 minutes each
    
    # Calculate the number of 2-point shots John makes
    num_2pt_shots = (total_time / 4) * 2
    
    # Calculate the number of 3-point shots John makes
    num_3pt_shots = (total_time / 4)
    
    # Calculate the total points John scores
    total_points = (num_2pt_shots * 2) + (num_3pt_shots * 3)
    
    result = total_points
    return result

print(solution())