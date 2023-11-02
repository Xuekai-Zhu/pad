def solution():
    total_show_time = 2 * 60  # convert 2 hours to minutes
    stage_time = 6  # minutes
    exit_time = 2  # minutes
    intermission_time = 10  # minutes

    # Calculate the total time Vicki spends on stage and exit
    total_stage_time = stage_time + exit_time

    # Calculate the remaining time for the show
    remaining_time = total_show_time - total_stage_time

    # Calculate the number of groups Vicki can perform in the concert
    num_groups = remaining_time // intermission_time
    result = num_groups
    return result

print(solution())