def solution():
    """Two runners are competing in a 10-mile race. The first runs at an average pace of 8 minutes per mile, while the second runs at an average pace of 7 minutes per mile. After 56 minutes, the second runner stops for a drink of water. For how many minutes could the second runner remain stopped before the first runner catches up with him?"""
    race_distance = 10
    first_runner_pace = 8
    second_runner_pace = 7
    time_to_catch_up = (56 / 60) + (race_distance / second_runner_pace)
    remaining_time = (race_distance / first_runner_pace) - time_to_catch_up
    result = remaining_time * 60
    return result

print(solution())