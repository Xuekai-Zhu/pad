def solution():
    
    # Define the distance of each runner
    runner1_distance = 400
    runner2_distance = 60
    runner3_distance = runner1_distance + 3

    # Calculate the total distance of the first runner
    first_runner_distance = runner1_distance * 4

    # Calculate the total distance of the second runner
    second_runner_distance = runner2_distance * 4

    # Calculate the difference in time between the two teams
    time_difference = first_runner_distance - second_runner_distance

    # Return the result
    result = time_difference
    return result

print(solution())