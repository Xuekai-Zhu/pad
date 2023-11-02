def solution():
    """Frank is walking through a corn maze. He has already spent 45 minutes inside. 
    He has done 4 other corn mazes and finished those in 50 minutes on average. 
    How much longer can he spend inside if he wants to ensure that his average 
    doesn't go above 60 minutes per maze?"""
    num_mazes = 5
    current_total_time = 45 + (4 * 50)  # time spent in current and previous mazes
    max_avg_time = 60  # maximum average time per maze
    max_total_time = num_mazes * max_avg_time  # maximum total time allowed for all mazes

    remaining_time = max_total_time - current_total_time  # time remaining for current maze
    result = remaining_time
    return result

print(solution())