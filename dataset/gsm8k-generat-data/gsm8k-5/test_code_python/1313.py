def solution():
    average_time_per_maze = 50  # Frank finished 4 other mazes in 50 minutes on average
    total_time_spent_in_other_mazes = average_time_per_maze * 4  # Frank spent a total of 200 minutes in other mazes
    maximum_allowed_time_in_this_maze = 60  # Frank wants to ensure his average time per maze doesn't go above 60 minutes
    current_time_spent_in_this_maze = 45  # Frank has already spent 45 minutes in this maze

    # Calculate the maximum time Frank can spend inside this maze
    remaining_time = maximum_allowed_time_in_this_maze * 5 - total_time_spent_in_other_mazes - current_time_spent_in_this_maze
    result = remaining_time
    return result

print(solution())