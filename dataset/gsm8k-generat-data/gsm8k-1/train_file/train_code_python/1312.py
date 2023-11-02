def solution():
    """Frank is walking through a corn maze. He has already spent 45 minutes inside. 
    He has done 4 other corn mazes and finished those in 50 minutes on average. 
    How much longer can he spend inside if he wants to ensure that his average doesn't go above 60 minutes per maze?"""
    
    avg_time_per_maze = 50
    total_mazes_completed = 4
    current_total_time = avg_time_per_maze * total_mazes_completed + 45
    total_mazes = 5
    max_avg_time = 60
    remaining_time = max_avg_time * total_mazes - current_total_time
    result = remaining_time
    return result

print(solution())