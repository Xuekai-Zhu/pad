def solution():
    race_distance = 10  # The race distance is 10 miles
    first_runner_pace = 8  # The first runner is running at a pace of 8 minutes per mile
    second_runner_pace = 7  # The second runner is running at a pace of 7 minutes per mile
    time_elapsed = 56  # The second runner stopped for 56 minutes

    # Calculate how far each runner has run after 56 minutes
    first_runner_distance = first_runner_pace * (56 / 60)
    second_runner_distance = second_runner_pace * (56 / 60)

    # Calculate how much farther the first runner is ahead of the second runner after 56 minutes
    distance_ahead = first_runner_distance - second_runner_distance

    # Calculate how long the second runner can remain stopped before being caught up with
    time_to_catch_up = (distance_ahead / (first_runner_pace - second_runner_pace)) * 60

    result = time_to_catch_up - time_elapsed
    return result

print(solution())