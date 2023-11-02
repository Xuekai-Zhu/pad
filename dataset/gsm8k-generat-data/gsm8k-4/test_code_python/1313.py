def solution():
    """Frank is walking through a corn maze. He has already spent 45 minutes inside. He has done 4 other corn mazes and finished those in 50 minutes on average. How much longer can he spend inside if he wants to ensure that his average doesn't go above 60 minutes per maze?"""
    # Define the current total time
    current_time = 45 + (4 * 50)

    # Define the number of mazes completed
    num_mazes = 5

    # Define the maximum average time per maze
    max_avg_time = 60

    # Calculate the maximum total time Frank can spend in the current maze
    max_maze_time = (max_avg_time * num_mazes) - current_time

    # Return the result
    result = max_maze_time
    return result

print(solution())