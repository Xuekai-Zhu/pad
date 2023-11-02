def solution():
    first_runner_time = 21 # minutes to run 3 miles
    second_runner_time = 24 # minutes to run 3 miles

    # Average out the time it takes to run 1 mile (based on running 3 miles)
    first_runner_pace = first_runner_time / 3 # minutes per mile
    second_runner_pace = second_runner_time / 3 # minutes per mile
    average_pace = (first_runner_pace + second_runner_pace) / 2 # minutes per mile

    # Calculate the total time it will take for each runner to run 5 miles
    first_runner_total_time = 5 * first_runner_pace # minutes
    second_runner_total_time = 5 * second_runner_pace # minutes

    # Add the total times for each runner to get the combined time
    combined_time = first_runner_total_time + second_runner_total_time # minutes
    result = combined_time
    return result

print(solution())