def solution():
    num_mazes = 5  # including the current one
    current_time = 45
    average_time_per_maze = 50
    max_average_time = 60

    # Calculate the total time spent on all previous mazes
    total_previous_time = (num_mazes - 1) * average_time_per_maze

    # Calculate the maximum time allowed for the current maze
    max_allowed_time = max_average_time * num_mazes - total_previous_time - current_time

    result = max_allowed_time
    return result

print(solution())