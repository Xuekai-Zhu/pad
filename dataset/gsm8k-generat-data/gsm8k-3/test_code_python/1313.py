def solution():
    """Frank is walking through a corn maze. He has already spent 45 minutes inside. He has done 4 other corn mazes and finished those in 50 minutes on average. How much longer can he spend inside if he wants to ensure that his average doesn't go above 60 minutes per maze?"""
    # Define the number of completed mazes and the average time per maze
    completed_mazes = 4
    avg_time = 50

    # Calculate the total time spent on completed mazes
    total_time = completed_mazes * avg_time

    # Define the desired average time per maze
    desired_avg = 60

    # Calculate the maximum time Frank can spend in the current maze
    max_time = (desired_avg * (completed_mazes + 1)) - total_time - 45

    # Display the maximum time
    result = max_time
    return result

print(solution())