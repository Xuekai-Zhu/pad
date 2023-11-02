def solution():
    """Two runners are competing in a 10-mile race. The first runs at an average pace of 8 minutes per mile, while the second runs at an average pace of 7 minutes per mile. After 56 minutes, the second runner stops for a drink of water. For how many minutes could the second runner remain stopped before the first runner catches up with him?"""
    race_distance = 10
    first_runner_pace = 8
    second_runner_pace = 7
    first_runner_time = race_distance * first_runner_pace
    second_runner_time = 0
    time_elapsed = 0

    while second_runner_time + second_runner_pace < first_runner_time:
        second_runner_time += second_runner_pace
        time_elapsed += 1

        if time_elapsed == 56:
            second_runner_time += 5

    result = 60 - ((second_runner_time + second_runner_pace) - first_runner_time) % 60
    return result

print(solution())