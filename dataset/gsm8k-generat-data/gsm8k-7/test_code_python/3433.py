def solution():
    race_distance = 10
    first_runner_pace = 8  # minutes per mile
    second_runner_pace = 7  # minutes per mile
    second_runner_stop_time = 0  # minutes
    
    # Calculate the distance covered by the first runner after 56 minutes
    first_runner_distance = (56 / first_runner_pace)

    # Calculate the remaining distance still to be covered by both runners
    remaining_distance = race_distance - first_runner_distance

    # Calculate the time it would take for the second runner to cover the remaining distance without stopping
    time_to_finish = remaining_distance * second_runner_pace

    # Calculate the time the second runner has remaining after stopping, before the first runner catches up
    second_runner_stop_time = time_to_finish - (56 - second_runner_stop_time)

    result = second_runner_stop_time
    return result

print(solution())