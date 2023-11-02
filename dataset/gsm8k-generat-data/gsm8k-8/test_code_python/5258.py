def solution():
    # Define the daily distances and the total number of days for each phase
    phase1_distance = 5
    phase1_days = 30
    phase2_distance = 10
    phase2_days = 30
    phase3_distance = 20
    phase3_days = 30
    
    # Calculate the total distance for each phase
    phase1_total_distance = phase1_distance * phase1_days
    phase2_total_distance = phase2_distance * phase2_days
    phase3_total_distance = phase3_distance * phase3_days
    
    # Calculate the total distance run during the 90 days
    total_distance = phase1_total_distance + phase2_total_distance + phase3_total_distance
    result = total_distance
    return result

print(solution())