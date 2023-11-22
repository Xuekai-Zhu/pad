def solution():
    
    # Define the total time the show will last in minutes
    total_time = 2 * 60

    # Define the time it takes for each group to complete the task
    stage_time = 2
    perform_time = 6
    exit_time = 2

    # Define the time Vicki allows for the intermission
    intermission_time = 10

    # Calculate the total time the groups can perform
    total_time_per_group = stage_time + perform_time + exit_time
    total_groups = total_time // total_time_per_group

    # return the result
    result = total_groups
    return result

print(solution())