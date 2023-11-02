def solution():
    # Define the variables
    total_distance = 10
    first_runner_pace = 8
    second_runner_pace = 7
    second_runner_stop = 56
    time_elapsed = 0

    # Calculate the time it takes for the first runner to complete the race
    first_runner_time = total_distance * first_runner_pace

    # Calculate the time it takes for the second runner to reach the point where they stop for water
    second_runner_time_before_stop = (total_distance / second_runner_pace) * 60
    time_elapsed += second_runner_time_before_stop

    # Calculate the time it takes for the first runner to catch up with the second runner
    distance_covered_by_second_runner = (second_runner_time_before_stop / 60) * second_runner_pace
    time_elapsed += (distance_covered_by_second_runner / first_runner_pace) * 60

    # Calculate the time the second runner can remain stopped before being caught up with
    remaining_time = ((total_distance - distance_covered_by_second_runner) / second_runner_pace) * 60
    result = remaining_time - second_runner_stop
    return result

print(solution())