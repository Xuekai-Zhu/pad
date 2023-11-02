def solution():
     painting_time = 4 * 1  # 1 hour per painting
     setup_time = 1  # 1 hour for setup
     cleanup_time = 1  # 1 hour for cleanup
     editing_time = 4 * 1.5  # 1.5 hours per video
 
     total_time = painting_time + setup_time + cleanup_time + editing_time
 
     result = total_time
 
     return result

print(solution())